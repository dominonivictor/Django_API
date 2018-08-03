from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

#inherithing viewsets from rest_framework

class TaskView(viewsets.ModelViewSet):
    #Pre standar methods in APIs: Get, Put, Delete
    queryset = Task.objects.all() #Gets all Task objects from the db
    serializer_class = TaskSerializer
