from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
from .forms import codeForm
import subprocess , os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def interview(request, interviewer, system_generated_id=11):
   #  if request.method == 'POST':
   #      form = codeForm(request.POST)
   #      if form.is_valid():
   #          code=form.cleaned_data['code']
   #          code1={'code':code}
   #          filename='code.py'
   #          file = open(filename,'w') 
   #          file.write(code1['code']) 
   #          file.close() 
   #          cmd = 'timelimit -t1 -pq python {}'.format(filename)
   #          if not subprocess.call(cmd,shell=True):
   #              print(subprocess.check_output(cmd,shell=True))
   #          else:
   #              print('crossed time limit')
   #  else:
   #      room_name = f"{interviewer}{system_generated_id}"
   #      form = codeForm()
    form = codeForm()
    room_name = f"{interviewer}{system_generated_id}"
    return render(request,'interview.html',{ 'room_name': room_name, 
            'room_name_json': mark_safe(json.dumps(room_name)), 'man': mark_safe(json.dumps(interviewer)),'form':form})

@csrf_exempt
def compile_code(request):
   #  code1 = json.loads(request.body)
   code = request.POST.get('code', None)
   print(code)
   filename='code.py'
   file = open(filename,'w')
   file.write(code)
   file.close()
   cmd = 'timelimit -t1 -pq python {}'.format(filename)
   # x=subprocess.call(cmd,shell=True)
   # print(x)
   
   if not subprocess.call(cmd,shell=True):
         output=subprocess.check_output(cmd,shell=True)
         result = {
            'output' : output,
            'status' : 'compiled succesfully'
         }
   else:
         result = {
            # 'output' : os.popen('python code.py').read(),
            'status' : 'timed out'
         }

   # try:
   #    if not subprocess.call(cmd,shell=True):
   #       output=subprocess.check_output(cmd,shell=True)
   #       result = {
   #          'output' : output,
   #          'status' : 'compiled succesfully'
   #       }
   #    else:
   #       result = {
   #          'output' : subprocess.check_output(cmd,shell=True),
   #          'status' : 'timed out'
   #       }
   # except:
   #    result={
   #       'error' : 'error'
   #    }
   print(result)
   return mark_safe(json.dumps(result))