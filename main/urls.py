from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compile_code',views.compile_code,name='compile_code'),
    path('interview/<interviewer><system_generated_id>', views.interview, name='interview'),
]