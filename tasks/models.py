from asyncio.windows_events import NULL
from datetime import date
from django.conf import settings
from django.db import models
from  django.contrib.auth.models import User



class Board (models.Model):
    name = models.CharField(max_length=500)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_at = models.DateField(default=date.today)
    def __str__(self):
        return "{0}".format(self.name)

class Task(models.Model):
    status= models.ForeignKey(to='status',on_delete=models.CASCADE)
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=512, null=True, blank=True)
    created_at = models.DateField(default=date.today)
    color = models.CharField(max_length=512, null=True, blank=True)
    urgency = models.CharField(max_length=512, null=True, blank=True)
    category = models.CharField(max_length=512, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{0}".format(self.title)

class Status(models.Model):
    status_choices = [
        ('todo','todo'),
    ('working', 'working'),
    ('done','done'),
    ]
    status=models.CharField(max_length = 20, choices= status_choices, default='todo')
    def __str__(self):
        return "{0}".format(self.status)

