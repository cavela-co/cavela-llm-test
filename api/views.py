from django.shortcuts import render, redirect, get_object_or_404
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


def add_question(request, file_id):
    if request.method == "POST":
        try:
            # Parse the JSON data
            data = json.loads(request.body)
            question = data.get("question", "").strip()

            if not question:
                return JsonResponse({"success": False, "error": "Question is required"}, status=400)

            # Get the file object
            file_obj = get_object_or_404(UploadedFile, id=file_id)

            # Initialize questions list if not exists
            if not file_obj.questions:
                file_obj.questions = []

            # Add the new question
            file_obj.questions.append(question)

            # Save the file object
            file_obj.save()

            return JsonResponse({"success": True})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Method not allowed"}, status=405)
