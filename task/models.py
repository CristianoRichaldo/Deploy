from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50, default="названия нет")
    description = models.TextField(blank=True, default="описания нет")
