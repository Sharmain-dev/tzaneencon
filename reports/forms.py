from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['issue_type', 'description', 'photo', 'location']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Please describe the issue in detail...'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'e.g., 25 Dan Village, Tzaneen'
            }),
        }