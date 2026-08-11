from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

class TaskView(APIView):
    def get(self, request):
        data = TaskSerializer(Task.objects.all(), many=True).data
        return Response(data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status = status.HTTP_201_CREATED)
