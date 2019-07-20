from django.conf import settings
from django.db import models
from django.utils import timezone


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
