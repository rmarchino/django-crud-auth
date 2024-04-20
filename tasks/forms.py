from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese título'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input mb-3'})
        }
