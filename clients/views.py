from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Client
from .serializers import ClientSerializer, TaskSerializer
# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer