from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compile_code',views.compile_code,name='compile_code'),
    path('interview/<interview_id>', views.interview, name='interview'),
    path('generate_interview/', views.generate_interview, name='generate_interview'),
    path('join_interview/', views.join_interview, name='join_interview'),
    # path('verify_mail/', views.verify_mail, name='verify_mail'),
]