from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from .forms import codeForm
import subprocess , os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import hashlib
from django.contrib.auth.models import User
from .models import InterviewList


def index(request):
   user_email = 'anonymous'
   if request.user.is_authenticated:
      user_email = request.user.email
   return render(request,'index.html', { 'user_mail': mark_safe(json.dumps(user_email))})

@login_required(login_url='login')
def interview(request, interview_id):
   form = codeForm()
   room_name = interview_id
   
   return render(request,'interview.html',{ 'room_name': room_name, 
           'room_name_json': mark_safe(json.dumps(room_name)), 'man': mark_safe(json.dumps(request.user.first_name)),'form':form})


def compile_code(request):
   #  code1 = json.loads(request.body)
   code = request.POST.get('code', None)
   print(code)
   filename='code.py'
   file = open(filename,'w')
   file.write(code)
   file.close()
   cmd = 'timelimit -t1 -pq python {}'.format(filename)
   
   try:
      if not subprocess.call(cmd,shell=True):
            output=subprocess.check_output(cmd,shell=True)
            result = {
               'output' : str(output),
               'status' : 'compiled succesfully'
            }
      else:
            result = {
               # 'output' : os.popen('python code.py').read(),
               'output' : 'timed out',
               'status' : 'error'
            }
   except:
      result={
         'output' : 'error',
         'status' : 'error'
      }
   print(result)
   return JsonResponse(result)

@csrf_exempt
def generate_interview(request):
   candidate_mail = request.POST.get('candidate_mail', None)
   interviewer_mail = request.user.email
   interview = InterviewList()
   interview.interviewer = request.user
   interview.candidate = candidate_mail
   interview.save()
   hash_interviewer = hashlib.md5(interviewer_mail.encode()).hexdigest()
   hash_candidate = hashlib.md5(candidate_mail.encode()).hexdigest()
   data = {
      'hashedValue': hash_interviewer + hash_candidate
   }
   return JsonResponse(data)

@csrf_exempt
def join_interview(request): 
   candidate_mail = request.user.email
   if InterviewList.objects.filter(candidate=candidate_mail.lower()).exists():
      interview = InterviewList.objects.filter(candidate=candidate_mail.lower()).first()
      interviewer_mail = interview.interviewer.email
      active = True
   else:
      interviewer_mail = '#'
      active = False
   hash_interviewer = hashlib.md5(interviewer_mail.encode()).hexdigest()
   hash_candidate = hashlib.md5(candidate_mail.encode()).hexdigest()
   data = {
      'active': active,
      'hashedValue': hash_interviewer + hash_candidate
   }
   return JsonResponse(data)

# same as encrypt_text 
# def encrypt(plaintext):
#    hashValue = hashlib.md5(plaintext.encode())
#    return hashValue.hexdigest()

# def verify_mail(request):
#    mail = request.GET.get('mail', None)
#    if User.objects.filter(email=mail.lower()).exists():
#       data = {'registered': True}
#    else:
#       data = {'registered': False}   
#    return JsonResponse(data)
