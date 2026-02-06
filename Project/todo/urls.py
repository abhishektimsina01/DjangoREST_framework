from django.urls import path, include
from .views import getAllTodos, deleteAll, add_todo, updateTodo, addUsers, getAllUsers, updateUser
from .views import TodoClass, TodoGenericClass, TodoPreBuiltGenericClass, TodoViewSet, TodoModelViewSet, TodoAuthenticated
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

router = DefaultRouter()
router.register('data', TodoViewSet, basename='data')
router.register('todo', TodoModelViewSet, basename="todo")
router.register('todoAuth', TodoAuthenticated, basename="todoAuth")

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
    path('update/<uuid:id>', TodoClass.as_view()),

    path('readTodo/', TodoGenericClass.as_view()),
    path('postTodo', TodoGenericClass.as_view()),
    path('deleteTodo/<uuid:pk>', TodoGenericClass.as_view()),
    path('updateTodo/<uuid:pk>', TodoGenericClass.as_view()),

    path("readTodos/", TodoPreBuiltGenericClass.as_view()),

    path("", include(router.urls)),
]
