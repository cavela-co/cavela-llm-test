from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task, UploadedFile
from .forms import FileUploadForm


def task_list(request):
    tasks = Task.objects.all().values(
        "id", "title", "description", "completed", "created_at"
    )
    return JsonResponse(list(tasks), safe=False)


def home(request):
    return render(request, "home.html", {"title": "Django Tasks API"})


def upload_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("file_list")
    else:
        form = FileUploadForm()

    return render(request, "upload_file.html", {"form": form, "title": "Upload File"})


def file_list(request):
    files = UploadedFile.objects.all().order_by("-uploaded_at")
    return render(
        request, "file_list.html", {"files": files, "title": "Uploaded Files"}
    )
