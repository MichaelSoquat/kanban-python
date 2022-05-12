from django.contrib import admin
from django.urls import path

from .views import tasks_view, login_view, register_view, redirect, logout_view

urlpatterns = [
    path('', redirect),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view, name="register"),
    path('tasks/', tasks_view),
    path('logout/', logout_view, name="logout")
]