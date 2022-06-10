
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from tasks.models import Task
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import Board, Task, Token
from .serializers import BoardSerializer, TaskSerializer

# TEST WITH CREATE TOKEN WHEN USER REGISTERED
def testHtml(request): 
    return render(request, "main/board.html")


# BOARD CREATE, READ, UPDATE, DELETE

@login_required(login_url='/login/')
@api_view(['GET'])
# @renderer_classes([JSONRenderer])
# @renderer_classes([TemplateHTMLRenderer])

def boards(request):
    boards= Board.objects.all()
    serializer = BoardSerializer(boards, many = True)
    return Response({'boards':serializer.data})

# template_name='main/board.html'
    
@api_view(['GET'])
def board(request, pk):
    board= Board.objects.get(id=pk)
    tasks= Task.objects.filter(board__id = pk)
    serializer_board = BoardSerializer(board, many = False)
    serializer_tasks = TaskSerializer(tasks, many=True)
    return Response(data = [serializer_board.data, serializer_tasks.data])

@api_view(['POST'])
def boardCreate(request):
    
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def boardUpdate(request, pk):
    board = Board.objects.get(id=pk)
    serializer = BoardSerializer(instance = board, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def boardDelete(request,pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return Response('Board deleted')


# TASKS CREATE, READ, UPDATE, DELETE


@api_view(['GET'])
def taskDetail(request, board_pk, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request, board_pk,):
    request.data['board']=board_pk
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def taskUpdate(request, board_pk, pk):
    request.data['board']=board_pk
    task = Task.objects.get(id= pk)
    serializer = TaskSerializer(instance = task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, board_pk, pk):
    task = Task.objects.get(id= pk)
    task.delete()
    return Response('Task deleted')


# LOGIN, LOGOUT, REGISTER
    """
    The login function matches the authentication to log in successfully.
    """ 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user: 
        login(request, user)
        token = Token.objects.get(User=user)
        print(token)
        return HttpResponse("You are authenticated")
    else:
        return HttpResponse("Invalid Data")

    """
    With the post method, new users can be added by providing such as username, email, password.
    For the existing Django user model.
    """
@csrf_exempt
def register_view(request):
    if request.method == "POST":
        
        
        first_name=request.POST.get("first_name")
        username=request.POST.get("username")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        password_repeat=request.POST.get("password_repeat")
        email=request.POST.get("email")
            
        
        if password == password_repeat:
            print("create user")
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                token = Token.objects.get(user=user).key

                if user: 
                    login(request,user)
                    print(token)
                             
                return JsonResponse({"token": token}, safe=False)
            except IntegrityError:
                return JsonResponse({"errorMessage": "Username already exists" }, safe=False) 
        else:
            return JsonResponse({"errorMessage": "Passwords don't match" }, safe=False)
         
        
    return HttpResponse('run /test/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')




