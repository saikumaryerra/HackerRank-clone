from django.conf import settings
from django.db import models
<<<<<<< HEAD
from django.utils import timezone

||||||| merged common ancestors
=======
from django.contrib.auth.models import User
from datetime import datetime
>>>>>>> fe0b1464372731e4284092e6ea94555dfc9608bc

<<<<<<< HEAD
# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length = 30)
    interviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    score = models.IntegerField(default=0)

class Message(models.Model):
    interview = models.ForeignKey(Interview , on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class Code(models.Model):
    code = models.TextField()
    interview = models.ForeignKey(Interview,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
||||||| merged common ancestors
# Create your models here.
=======

class InterviewList(models.Model):
   interviewer = models.ForeignKey(User, related_name= 'iv', on_delete=models.CASCADE)
   candidate = models.ForeignKey(User, related_name= 'cd', on_delete=models.CASCADE)
   score = models.IntegerField(default=0)
   created_on = models.DateTimeField(default=datetime.now())
   active = models.BooleanField(default=True)
   link = models.CharField(max_length=256)

class Room(models.Model):
   roomname = models.TextField()
   users = models.IntegerField(default=0)
#    def __str__(self):
#       return self.roomname

class RoomMember(models.Model):
   name = models.CharField(max_length=300)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
#    def __str__(self):
    #   return self.room
>>>>>>> fe0b1464372731e4284092e6ea94555dfc9608bc
