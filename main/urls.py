from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compile_code',views.compile_code,name='compile_code'),
    path('interview/<interview_id>', views.interview, name='interview'),
    path('generate_interview/', views.generate_interview, name='generate_interview'),
    path('join_interview/', views.join_interview, name='join_interview'),
    path('interview_list/', views.interview_list, name='interview_list'),
    path('interview_list/deactivate_link/', views.deactivate_link, name='deactivate_link'),
    path('interview/deactivate_link/', views.deactivate_link, name='deactivate_link'),
]