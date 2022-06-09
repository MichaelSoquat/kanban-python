from rest_framework import serializers
from .models import Board, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Board
        fields = '__all__'