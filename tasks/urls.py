from django.contrib import admin
from django.urls import path

from .views import boards, board, boardUpdate, login_view, register_view, logout_view, api_view, taskDetail, taskCreate, taskUpdate, taskDelete, boardDelete, boardCreate
from .views import testHtml
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    
   
    path("test/", testHtml), 
    # Admin, Register, Login, Logout
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),
    path('register/', register_view, name="register"),
    path('logout/', logout_view, name="logout"),

    #  Board
    path('board/', boards),
    path('board/<int:pk>/', board),
    path('board/create/', boardCreate),
    path('board/<int:pk>/update', boardUpdate),
    path('board/<int:pk>/delete', boardDelete),

    # Tasks

    path('board/<int:board_pk>/task-detail/<int:pk>/', taskDetail),
    path('board/<int:board_pk>/task-create/', taskCreate, name ='task-create'),
    path('board/<int:board_pk>/task-update/<int:pk>/', taskUpdate, name ='task-update'),
    path('board/<int:board_pk>/task-delete/<int:pk>/', taskDelete, name ='task-delete'),
]



# Improve fields of models
