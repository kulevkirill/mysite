from django.shortcuts import render
from django.core.cache import cache

from . import tasks_utils

def index(request):
    return render(request, "index.html")

def task_list(request):
    tasks = tasks_utils.get_tasks()
    return render(request, "task_list.html", context={"tasks": tasks})

def add_task(request):
    return render(request, "add_task.html")

def send_task(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_task = request.POST.get("new_task", "").replace(";", ",")
        new_answer = request.POST.get("new_answer", "") # def -> answer, term -> task
        context = {"user": user_name}
        if len(new_answer) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_task) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            tasks_utils.write_task(new_task, new_answer)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "task_request.html", context)
    else:
        add_task(request)