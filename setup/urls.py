from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdateView # Importando o CBV - Class Basic View 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name='todo_list'), # SEMPRE PASSAR O .AS_VIEW() NA CBV
    path("create", TodoCreateView.as_view(), name='todo_create'),
    path("update/<int:pk>", TodoUpdateView.as_view(), name='todo_update'),# Passar a PK para direcionar a uma tarefa específica

]
