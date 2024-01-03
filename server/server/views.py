from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def todo_list(request):
    items = TodoItem.objects.all().values()
    items_list = list(items)
    return JsonResponse({'items': items_list})

@csrf_exempt
def add_todo_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item = TodoItem.objects.create(
                title=data['title'],
                description=data['description'],
                completed=data.get('completed', False),
                due_date=data.get('due_date')
            )
            return JsonResponse({'id': item.id}, status=201)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def edit_todo_item(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            item = TodoItem.objects.get(pk=id)
            item.title = data.get('title', item.title)
            item.description = data.get('description', item.description)
            item.completed = data.get('completed', item.completed)
            item.due_date = data.get('due_date', item.due_date)
            item.save()
            return JsonResponse({'message': 'Item updated successfully'})
        except TodoItem.DoesNotExist:
            return HttpResponse("Item not found", status=404)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON", status=400)
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def delete_todo_item(request, id):
    TodoItem.objects.get(pk=id).delete()
    return redirect('todo_list')
