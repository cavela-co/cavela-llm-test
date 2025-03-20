from django import forms
from .models import UploadedFile


class FileUploadForm(forms.ModelForm):
    # Add a hidden field for questions that will be populated via JavaScript
    questions = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UploadedFile
        fields = ["file", "title", "description", "questions"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }
