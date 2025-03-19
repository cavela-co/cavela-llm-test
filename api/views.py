from django.shortcuts import render
from django.http import JsonResponse
from .models import Task


def task_list(request):
    tasks = Task.objects.all().values(
        "id", "title", "description", "completed", "created_at"
    )
    return JsonResponse(list(tasks), safe=False)


def home(request):
    return render(request, "home.html", {"title": "Django Tasks API"})
