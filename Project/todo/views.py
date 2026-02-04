from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer, UserSerializer
from .models import Todos, User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET'])
def getAllTodos(request):
    print(request.GET)
    todos = Todos.objects.all()
    serialized = TodoSerializer(todos, many = True)
    return Response(data = serialized.data, status= status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteAll(request, id):
    try:
        res = Todos.objects.get(id = id)
    except Todos.DoesNotExist:
        return Response({'error' : 'issue'}, status=status.HTTP_404_NOT_FOUND)
    Todos.objects.all().delete()
    return Response({"message" : 'removed the todo list'}, status= status.HTTP_200_OK)


@api_view(['POST'])
def add_todo(request):
    print(request.POST)
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['PUT'])
def updateTodo(request, id):
    try: 
        todo = Todos.objects.get(id = id)
    except:
        return Response({'error' : 'The task does not exist'})
    print(todo)
    serializer = TodoSerializer(
        todo,
        data = request.data,
        partial = True,
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# **********************************************************************************************************************


@api_view(['POST'])
def addUsers(request):
    print(request.data)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def getAllUsers(request):
    try:
        users = User.objects.all()
    except:
        return Response({'error' : 'No user found'})
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, id):
    data  = request.data
    try:
        user = User.objects.get(id = id)
    except:
        return Response({'error' : 'User not found'})
    serializer = UserSerializer(instance = user, data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.validated_data)
    return Response(serializer.errors)


# **********************************************************************************************************************


# class based view
class TodoClass(APIView):
    
    def get(request):
        todos = Todos.objects.all()
        serializer = TodoSerializer(todos, many = True)
        return Response(data = serializer, status= status.HTTP_200_OK)

    def post(request):
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        return Response(data = serializer.errors)

    def delete(request, id):
        try:
            todo = Todos.objects.get(id = id).delete()
        except Todos.DoesNotExist:
            return Response({'error' : "doesnot exist"}, status= status.HTTP_404_NOT_FOUND)
        return Response({'message' : "todo deleted"}, status=status.HTTP_200_OK)
    
    def put(request, id):
        data = request.data
        try:
            todo = Todos.objects.get(id = id)
        except Todos.DoesNotExist:
            return Response({'error' : 'Doesnot exist'})
        serializer = TodoSerializer(instance = todo, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)