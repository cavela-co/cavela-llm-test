from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/tasks/", views.task_list, name="task_list"),
    path("upload/", views.upload_file, name="upload_file"),
    path("files/", views.file_list, name="file_list"),
    path("api/add_question/<int:file_id>/", views.add_question, name="add_question"),
]
