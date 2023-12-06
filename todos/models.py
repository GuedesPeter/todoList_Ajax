from django.db import models
from datetime import date


# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name='Título',max_length=100, null=False, blank=False)  # TITULO
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)  # DATA DE CRIAÇÃO
    deadline = models.DateField(verbose_name='Entregar em',null=False, blank=False)  # DATA DE ENTREGA
    finished_at = models.DateField(null=True, blank=False)  # DATA DE FINALIZAÇÃO

    #Classe para utilizar metadados (Filtros) - Neste caso para realizar ordenação por Data na Lista de Tarefas(ToDo)
    class Meta:
        ordering = ["deadline"]


    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()

