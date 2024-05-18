from django.shortcuts import render
from django.core.cache import cache

from . import tasks_utils

def index(request):
    return render(request, "index.html")

def task_list(request):
    tasks = tasks_utils.get_tasks()
    return render(request, "task_list.html", context={"tasks": tasks})
