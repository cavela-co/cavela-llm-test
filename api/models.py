from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FileType(models.TextChoices):
    QUOATATION = "QUOATATION"
    PROD_SPEC = "PROD_SPEC"
    QA_REPORT = "QA_REPORT"
    OTHER = "OTHER"


class UploadedFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=FileType.choices, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
