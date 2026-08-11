from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Books
from .serializers import BooksSerializers


class BookListApi(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
