from django.urls import reverse_lazy # Retorna as rotas de urls completas
from .models import Todo
# Utilizando o CBV - Class Basic View e importando classes genéricas para criar as Views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View # Importa uma classe genérica
from django.shortcuts import get_object_or_404, redirect

'''
Essa função é traduzida/equivalente a classe abaixo!!!
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todo': todos})
'''

# Classes Genéricas criadas

# READ
class TodoListView(ListView):
    model = Todo

# CREATE
class TodoCreateView(CreateView):
    model = Todo
    #Definir os campos que o usuário informará no cadastro
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

# UPDATE
class TodoUpdateView(UpdateView):
    model = Todo
    #Definir os campos que o usuário informará no cadastro
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

# DELETE
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete() # Metodo criado na model 
        return redirect('todo_list')
