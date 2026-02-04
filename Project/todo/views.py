from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todos
from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def getAllTodos(request):
    print(request.GET)
    todos = Todos.objects.all()
    serialized = TodoSerializer(todos, many = True)
    return Response(data = serialized.data)


@api_view(['DELETE'])
def deleteAll(request, id):
    try:
        res = Todos.objects.get(id = id)
    except:
        return Response({'error' : 'issue'})
    Todos.objects.get(id = id).delete()
    return Response({"message" : 'removed the todo list'})


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