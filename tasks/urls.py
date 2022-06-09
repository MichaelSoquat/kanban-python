from django.contrib import admin
from django.urls import path

from .views import boards, board, boardUpdate, login_view, register_view, redirect, logout_view, api_view, taskDetail, taskCreate, taskUpdate, taskDelete, boardDelete, boardCreate

urlpatterns = [
    # redirect if no url
    path('', redirect),

    # Admin, Register, Login, Logout
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),

    #  Board
    path('board/', boards),
    path('board/<str:pk>/', board),
    path('board/create/', boardCreate),
    path('board/<str:pk>/update', boardUpdate),
    path('board/<str:pk>/delete', boardDelete),

    # Tasks

    path('board/<str:board_pk>/task-detail/<str:pk>/', taskDetail),
    path('board/<str:board_pk>/task-create/', taskCreate, name ='task-create'),
    path('board/<str:board_pk>/task-update/<str:pk>/', taskUpdate, name ='task-update'),
    path('board/<str:board_pk>/task-delete/<str:pk>/', taskDelete, name ='task-delete'),
]



# Connect Board with tasks slugfield instead of id ?
# Improve fields of models
# Token?
# How to test