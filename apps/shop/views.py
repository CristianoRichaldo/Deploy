from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Shop
from .serializer import ShopSer
from .pagination import ShopPagination
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter

class ShopViewSets(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSer
    pagination_class = ShopPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'color']
    search_fields = ['name', 'color']
    ordering_fields = ['name', 'id']
    ordering = ['id']

    def get_permissions(self):
        """
        Разграничение прав доступа по действиям:
        - list, retrieve: доступ открыт всем пользователям (AllowAny)
        - create: только авторизованные пользователи (IsAuthenticated)
        - update, partial_update, destroy: только владелец объекта или админ (IsOwnerOrReadOnly)
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Автоматически привязываем текущего пользователя как владельца магазина
        """
        serializer.save(user=self.request.user)
