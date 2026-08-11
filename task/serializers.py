from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "title", "description")  
        read_only_fields = ("id",)

    def validate_title(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("поле title не может быть пустым")
        if len(value) < 3:
            raise serializers.ValidationError("минимум три символа в поле title")
        return value.strip()
