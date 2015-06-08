
from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    user_name = forms.CharField(label='',widget=forms.widgets.TextInput(attrs={'placeholder': 'patient Id'}))

    class Meta:
        model = Patient
        exclude = ('created_at',)
        