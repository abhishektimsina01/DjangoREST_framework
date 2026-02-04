from django.urls import path
from .views import getAllTodos, deleteAll, add_todo, updateTodo, addUsers, getAllUsers

urlpatterns = [
    path("getAll/", getAllTodos),
    path('deleteOne/<uuid:id>', deleteAll),
    path('addTodo', add_todo),
    path('updateTodo/<uuid:id>', updateTodo),
    path('addUser', addUsers),
    path("getAllUsers/", getAllUsers)
]
