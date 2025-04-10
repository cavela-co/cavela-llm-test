from django.db import models


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


class Quotation(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    moq = models.IntegerField()
    lead_time_days = models.IntegerField()
    payment_terms = models.CharField(max_length=200)
    shipping_method = models.CharField(max_length=200)
    shipping_address = models.TextField()


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
