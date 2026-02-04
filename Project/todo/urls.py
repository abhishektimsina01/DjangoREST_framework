from django.urls import path
from .views import getAllTodos, deleteAll, add_todo, updateTodo

urlpatterns = [
    path("getAll/", getAllTodos),
    path('deleteOne/<uuid:id>', deleteAll),
    path('addTodo', add_todo),
    path('updateTodo/<uuid:id>', updateTodo)
]
