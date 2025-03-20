from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    questions = models.JSONField(
        blank=True, null=True, help_text="A JSON list of questions related to this file"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
