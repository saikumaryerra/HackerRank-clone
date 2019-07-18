from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('interview/<interviewer><system_generated_id>', views.interview, name='interview'),
]