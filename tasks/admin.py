from django.contrib import admin

from tasks.models import Task, Status, Board

# Register your models here.
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Board)
