from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'project_deadline': forms.DateInput(attrs={'type': 'date'}),
        }
