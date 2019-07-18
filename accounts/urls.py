from django.urls import path
from django.contrib.auth import views
from . import views as view

urlpatterns = [
    path('signup/', view.signup, name='signup'),
    path('login/', view.login, name='login'),
    # path('logout/', view.logout, name='logout'),
]