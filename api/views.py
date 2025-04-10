from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, UploadedFile
from .forms import FileUploadForm
import json


def task_list(request):
    tasks = Task.objects.all().values("id", "title", "description", "completed", "created_at")
    return JsonResponse(list(tasks), safe=False)


def home(request):
    return render(request, "home.html", {"title": "Django Tasks API"})


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form instance but don't save to DB yet
            instance = form.save(commit=False)

            # Process the questions data from the hidden field
            questions_data = form.cleaned_data.get("questions", "")
            if questions_data:
                try:
                    # Convert the JSON string to a Python list
                    instance.questions = json.loads(questions_data)
                except json.JSONDecodeError:
                    instance.questions = []
            else:
                instance.questions = []

            # Save the instance with the processed data
            instance.save()
            return redirect("file_list")
    else:
        form = FileUploadForm()

    return render(request, "upload_file.html", {"form": form, "title": "Upload File"})


def file_list(request):
    files = UploadedFile.objects.all().order_by("-uploaded_at")
    return render(request, "file_list.html", {"files": files, "title": "Uploaded Files"})
