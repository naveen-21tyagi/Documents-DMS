from django import forms
from .models import Documents

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['title', 'uploadedFile']