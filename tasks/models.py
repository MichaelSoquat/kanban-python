from datetime import date
from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    status= models.ForeignKey(to='status',on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=512)
    created_at = models.DateField(default=date.today)

class Status(models.Model):
    status_choices = [
        ('todo','todo'),
    ('working', 'working'),
    ('done','done'),
    ]
    status=models.CharField(max_length = 20, choices= status_choices, default='todo')
    def __str__(self):
        return "{0}".format(self.status)


# settings.AUTH_USER_MODEL
