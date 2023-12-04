from django.contrib import admin
from django.urls import path

from todos.views import TodoListView, TodoCreateView # Importando o CBV - Class Basic View 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name='todo_list'), # SEMPRE PASSAR O .AS_VIEW() NA CBV
    path("create", TodoCreateView.as_view(), name='todo_create'),
   
]
