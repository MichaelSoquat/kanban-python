
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from tasks.models import Status
from tasks.models import Task
from django.core import serializers




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

def login_view(request):
    return render(request, 'auth/login.html')

def register_view(request):
    return render(request, 'auth/register.html')