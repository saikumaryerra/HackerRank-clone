from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json


# Create your views here.
def index(request):
    return render(request,'index.html')

def interview(request, interviewer, system_generated_id=11):
    room_name = f"{interviewer}{system_generated_id}"
    print(interviewer)
    return render(request,'interview.html',{ 'room_name': room_name, 
    'room_name_json': mark_safe(json.dumps(room_name)), 'man': mark_safe(json.dumps(interviewer))})