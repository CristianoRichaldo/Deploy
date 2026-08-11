from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here. APIView

class HelloApiView(APIView):
    def get(self, request):
        return Response({
            "message": "я Джанго Рест Фреймворк"
        })

class Profile(APIView):
    def get(self, request):
        return Response({
            "name": "Alisher",
            "age": "19",
            "group": "39-1B"
        })