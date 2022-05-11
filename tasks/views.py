
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




def redirect(request):
    return HttpResponseRedirect('tasks/')
# Create your views here.
def tasks_view(request):
    if request.method == 'POST':
         status = Status.objects.get(status = 'todo')
         task = Task.objects.create(title=request.POST['title'], 
         description=request.POST['description'], user=request.user, status=status)
         serialized_obj = serializers.serialize('json', [task,])
         return JsonResponse(serialized_obj[1:-1], safe=False)

    tasks= Task.objects.all()
    return render(request, 'main/tasks.html', {'tasks': tasks})


@login_required(login_url='/login/')
def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password= request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/tasks/')
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True,})
    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            user.date_joined = models.DateTimeField(default=datetime.now())
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect('/tasks/')
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