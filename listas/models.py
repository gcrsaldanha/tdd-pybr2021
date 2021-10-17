from django.db import models

# Create your models here.
class Tarefa(models.Model):
    texto = models.TextField(default='')
