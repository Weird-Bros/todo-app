from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    items = TodoItem.objects.all().values()
    items_list = list(items)
    return JsonResponse({'items': items_list})

def add_todo_item(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list') 
    else:
        form = TodoItemForm()
    return render(request, 'server/add_todo_item.html', {'form': form})

def edit_todo_item(request, id):
    item = TodoItem.objects.get(pk=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=item)
    return render(request, 'server/edit_todo_item.html', {'form': form})

def delete_todo_item(request, id):
    TodoItem.objects.get(pk=id).delete()
    return redirect('todo_list')
