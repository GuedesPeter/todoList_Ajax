from django.shortcuts import render
from django.urls import reverse_lazy # Retorna as rotas de urls completas
from .models import Todo
# Utilizando o CBV - Class Basic View e importando classes genéricas para criar as Views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # Importa uma classe genérica

'''
Essa função é traduzida/equivalente a classe abaixo!!!
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todo': todos})
'''

# Classe Genérica criada
class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    #Definir os campos que o usuário informará no cadastro
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    #Definir os campos que o usuário informará no cadastro
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
