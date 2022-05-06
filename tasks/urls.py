from django.contrib import admin
from django.urls import path

from .views import tasks_view, login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view),
    path('tasks/', tasks_view)
]