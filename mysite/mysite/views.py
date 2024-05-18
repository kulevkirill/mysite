from django.shortcuts import render
from django.core.cache import cache

import random

from . import tasks_utils

def index(request):
    return render(request, "index.html")

def task_list(request):
    tasks = tasks_utils.get_tasks()
    return render(request, "task_list.html", context={"tasks": tasks})

def solve_task(request):
    tasks = tasks_utils.get_tasks()
    task = tasks[random.randint(0, len(tasks)-1)]
    return render(request, "solve_task.html", context={"task": task[1], "answer": task[2]})

def send_answer(request):
    if request.method == "POST":
        cache.clear()
        answer = request.POST.get("answer", "")
        real_answer = request.POST.get("real_answer", "")
        context = {"answer": answer, "real_answer": real_answer}

        if answer == real_answer:
            context["success"] = True
            return render(request, "solved_task.html", context)

        context["success"] = False
        return render(request, "solved_task.html", context)

def add_task(request):
    return render(request, "add_task.html")

def send_task(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_task = request.POST.get("new_task", "").replace(";", ",")
        new_answer = request.POST.get("new_answer", "")
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

    add_task(request)
