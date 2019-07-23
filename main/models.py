from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


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
