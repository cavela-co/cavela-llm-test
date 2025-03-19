from django.contrib import admin
from .models import Task, UploadedFile

# Register your models here.
admin.site.register(Task)
admin.site.register(UploadedFile)
