from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .forms import TodoItemSerializer
from rest_framework import status

@api_view(['GET'])
def todo_list(request):
    """
    List all todo items.
    """
    todos = TodoItem.objects.all()
    serializer = TodoItemSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_todo_item(request):
    """
    Create a new todo item.
    """
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_todo_item(request, id):
    """
    Update an existing todo item identified by ID.
    """
    try:
        todo_item = TodoItem.objects.get(pk=id)
    except TodoItem.DoesNotExist:
        return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoItemSerializer(todo_item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_todo_item(request, id):
    """
    Delete a todo item identified by the given ID.
    """
    try:
        todo_item = TodoItem.objects.get(pk=id)
        todo_item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except TodoItem.DoesNotExist:
        return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
