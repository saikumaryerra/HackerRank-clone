from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import JsonResponse
import json
import hashlib
import datetime
from .forms import codeForm
import subprocess, os
from .models import InterviewList


def index(request):
   user_email = "anonymous"
   if request.user.is_authenticated:
       user_email = request.user.email
   return render(request, "index.html", {"user_mail": mark_safe(json.dumps(user_email))})


@login_required(login_url="login")
def interview(request, interview_id):
   form = codeForm()
   room_name = interview_id
   return render(
      request,
      "interview.html",
      {
          "room_name": room_name,
          "room_name_json": mark_safe(json.dumps(room_name)),
          "man": mark_safe(json.dumps(request.user.first_name)),
          "form": form,
      },
   )

@login_required(login_url="login")
def compile_code(request):
    #  code1 = json.loads(request.body)
    code = request.POST.get("code", None)
    print(code)
    filename = "code.py"
    file = open(filename, "w")
    file.write(code)
    file.close()
    cmd = "timelimit -t1 -pq python {}".format(filename)

    try:
        if not subprocess.call(cmd, shell=True):
            output = subprocess.check_output(cmd, shell=True)
            result = {"output": str(output), "status": "compiled succesfully"}
        else:
            result = {
                # 'output' : os.popen('python code.py').read(),
                "output": "timed out",
                "status": "error",
            }
    except:
        result = {"output": "error", "status": "error"}
    print(result)
    return JsonResponse(result)


@csrf_exempt
@login_required(login_url="login")
def generate_interview(request):
   signal = 200
   candidate_mail = request.POST.get("candidate_mail", None)
   if not User.objects.filter(email=candidate_mail.lower()).exists():
      signal = 404 #error code 404 - Not found
      data = {"signal": signal, "interview_link": "#"}
   elif candidate_mail == request.user.email:
      signal = 403 #error code 403 - Forbidden
      data = {"signal": signal, "interview_link": "#"}
   elif InterviewList.objects.filter(active=True).filter(candidate__email=candidate_mail).filter(interviewer__email=request.user.email).exists():
      signal = 401 #error code 401 - Unauthorized
      data = {"signal": signal, "interview_link": "#"}
   else:
      interviewer_mail = request.user.email
      # saving interview detail
      candidate = User.objects.filter(email=candidate_mail.lower()).first()
      interview = InterviewList()
      interview.interviewer = request.user
      interview.candidate = candidate
 
      hash_candidate = hashlib.md5(candidate_mail.encode()).hexdigest()
      date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      datetime_hash = hashlib.md5(date_time.encode()).hexdigest()
      interview_link = hash_candidate + datetime_hash
      interview.link = interview_link
      interview.save()

      data = {"signal": signal, "interview_link": interview_link}
   return JsonResponse(data)


@csrf_exempt
@login_required(login_url="login")
def join_interview(request):
   if InterviewList.objects.filter(candidate__email=request.user.email).filter(active=True).exists():
      data = {'active': True}
   else:
      data = {'active': False}
   return JsonResponse(data)


@csrf_exempt
@login_required(login_url="login")
def interview_list(request):
   links = []
   total = 0
   interview_links = InterviewList.objects.filter(candidate__email=request.user.email)|InterviewList.objects.filter(interviewer__email=request.user.email)
   for data in interview_links:
      links.append({
         'link': data.link,
         'interviewer': f'{data.interviewer.first_name} {data.interviewer.last_name}',
         'candidate': f'{data.candidate.first_name} {data.candidate.last_name}',
         'created_on': data.created_on.strftime("%Y-%m-%d %H:%M:%S"),
         'active': data.active
      })
      total = total + 1

   name = request.user.first_name + ' ' + request.user.last_name
   return render(request, 'interview_list.html', {'links': links, 'total': total, 'name': name})

@csrf_exempt
@login_required(login_url="login")
def deactivate_link(request):
   link = request.GET.get("link", None)
   interview = InterviewList.objects.filter(link=link).first()
   interview.active = False
   interview.save()
   return JsonResponse({})

