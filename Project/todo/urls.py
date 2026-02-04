from django.urls import path
from .views import getAllTodos, deleteAll, add_todo, updateTodo, addUsers, getAllUsers, updateUser
from .views import TodoClass

urlpatterns = [
    path("getAll/", getAllTodos),
    path('deleteOne/<uuid:id>', deleteAll),
    path('addTodo', add_todo),
    path('updateTodo/<uuid:id>', updateTodo),
    path('addUser', addUsers),
    path("getAllUsers/", getAllUsers),
    path('updateUser/<uuid:id>', updateUser),
    path('read/', TodoClass.as_view()),
    path('post', TodoClass.as_view()),
    path('delete/<uuid:id>', TodoClass.as_view()),
    path('update/<uuid:id>', TodoClass.as_view())
]
