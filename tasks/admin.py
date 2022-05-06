from django.contrib import admin

from tasks.models import task, status

# Register your models here.
admin.site.register(task)
admin.site.register(status)
