from django.contrib import admin
from django.urls import path

from .views import board, boardUpdate, login_view, register_view, redirect, logout_view, api_view, taskList, taskDetail, taskCreate, taskUpdate, taskDelete, boardDelete, boardCreate

urlpatterns = [
    # redirect if no url
    path('', redirect),

    # Admin, Register, Login, Logout
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),

    #  Board
    path('board/', board),
    path('board-create/', boardCreate),
    path('board-update/<str:pk>/', boardUpdate),
    path('board-delete/<str:pk>/', boardDelete),

    # Tasks

    path('task-list/', taskList, name ='task-list'),
    path('task-detail/<str:pk>/', taskDetail),
    path('task-create/', taskCreate, name ='task-create'),
    path('task-update/<str:pk>/', taskUpdate, name ='task-update'),
    path('task-delete/<str:pk>/', taskDelete, name ='task-delete'),
]