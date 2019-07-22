from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class InterviewList(models.Model):
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=datetime.now())
    active = models.BooleanField(default=True)
