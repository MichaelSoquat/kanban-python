from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def tasks_view(request):
    return HttpResponse('hi')

def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')