from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def redirect(request):
    return HttpResponseRedirect('tasks/')
# Create your views here.
def tasks_view(request):
    return render(request, 'main/tasks.html')

def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')