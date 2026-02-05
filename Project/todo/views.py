from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer, UserSerializer
from .models import Todos, User
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, ListAPIView



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
        users = User.objects.first()
    except:
        return Response({'error' : 'No user found'})
    serializer = UserSerializer(users,)
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
    
    def get(self, request, format = None):
        todos = Todos.objects.all()
        print(todos)
        serializer = TodoSerializer(todos, many = True)
        return Response(data = serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=status.HTTP_200_OK)
        return Response(data = serializer.errors)

    def delete(self, request, id):
        try:
            todo = Todos.objects.get(id = id).delete()
        except Todos.DoesNotExist:
            return Response({'error' : "doesnot exist"}, status= status.HTTP_404_NOT_FOUND)
        return Response({'message' : "todo deleted"}, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        data = request.data
        try:
            todo = Todos.objects.get(id = id)
        except Todos.DoesNotExist:
            return Response({'error' : "DoesNotExist"})
        serializer = TodoSerializer(instance = todo, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

# **********************************************************************************************************************

# GenericAPIView ans mixins

class TodoGenericClass(GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    def get(self, request):
        return self.list(request)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def post(self, request):
        return self.create(request)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    

# **********************************************************************************************************************

# pre-built generic views

class TodoPreBuiltGenericClass(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

# **********************************************************************************************************************

# Viewsets and ModelViewSet

class TodoViewSet(viewsets.ViewSet):

    def list(self, request):
        todo = Todos.objects.all()
        serializer = TodoSerializer(todo, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def create(self, request):
        # its the same, i am tired doing the same thing
        pass

    def retrieve(self, request, pk):
        try:
            todo = Todos.objects.get(id = pk)
        except Todos.DoesNotExist:
            return Response({'error' : 'DoesnotExist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(data = todo)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.validated_data)
        else:
            return Response(data = serializer.errors)
        
    def update(self, request, pk):
        data = request.data
        try:
            todo = Todos.objects.get(id = pk)
        except Todos.DoesNotExist:
            return Response({'error' : 'DoesNotExist'})
        serializer = TodoSerializer(data = data, instance = todo)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.validated_data)
        else:
            return Response(data = serializer.errors)


    def partial_update(self, request, pk):
        data = request.data
        try:
            todo = Todos.objects.get(id = pk)
        except Todos.DoesNotExist:
            return Response({'error' : 'DoesNotExist'})
        serializer = TodoSerializer(data = data, instance = todo ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data)
        else:
            return Response(data = serializer.errors)


    def destroy(self, response, pk):
        # its the same, i am tired doing the same thing
        pass

    @action(detail=False, methods=['GET'])
    def completed(self, request):
        todo = Todos.objects.filter(completed = True)
        serializer = TodoSerializer(todo, many = True)
        return Response(data=serializer.data)


# **********************************************************************************************************************

# ModelViewSet

class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['GET'])
    def completed(self, request):
        todo = Todos.objects.filter(completed = True)
        serializer = self.get_serializer(todo, many = True)
        return Response(data=serializer.data)