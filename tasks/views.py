
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from tasks.models import Status
from tasks.models import Task
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from datetime import date, datetime
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer

# REDIRECT
def redirect(request):
    return HttpResponseRedirect('board/')


# BOARD GET, CREATE, UPDATE, DELETE

@login_required(login_url='/login/')
@api_view(['GET'])
def board(request):
    boards= Board.objects.all()
    serializer = BoardSerializer(boards, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def boardCreate(request):
    
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def boardUpdate(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(board, many = False)
    return Response(serializer.data)

@api_view(['DELETE'])
def boardDelete(request,pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return Response('Board deleted')


# TASKS GET, CREATE, UPDATE, DELETE


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id= pk)
    serializer = TaskSerializer(instance = task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id= pk)
    task.delete()
    return Response('Task deleted')


# LOGIN, LOGOUT, REGISTER
    """
    The login function matches the authentication to log in successfully.
    """ 
def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password= request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/board/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True,})
    return render(request, 'auth/login.html')

    """
    With the post method, new users can be added by providing such as username, email, password.
    For the existing Django user model.
    """

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            user.date_joined = models.DateTimeField(default=datetime.now())
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect('/board/')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "auth/register.html",
                          context={"form":form})
    form = UserCreationForm
    return render(request = request,
                  template_name = "auth/register.html",
                  context={"form":form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')




