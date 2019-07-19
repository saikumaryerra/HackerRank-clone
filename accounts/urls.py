from django.urls import path, include
from django.contrib.auth import views
from . import views as view

urlpatterns = [
    path('signup/', view.signup, name='signup'),
    path('',include('django.contrib.auth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]