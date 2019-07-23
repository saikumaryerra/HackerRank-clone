from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class InterviewList(models.Model):
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)

class Room(models.Model):
   roomname = models.TextField()
   users = models.IntegerField(default=0)
#    def __str__(self):
#       return self.roomname

class RoomMember(models.Model):
   username = models.ForeignKey(User , on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   name = models.TextField()
   # def __str__(self):
   #    return self.room