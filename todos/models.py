from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)  # TITULO
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)  # DATA DE CRIAÇÃO
    deadline = models.DateField(null=False, blank=False)  # DATA DE ENTREGA
    finished_at = models.DateField(null=True, blank=False)  # DATA DE FINALIZAÇÃO
