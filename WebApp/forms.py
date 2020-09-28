from.models import cumpany
from django import forms

class NewForms(forms.ModelForm):
    class Meta:
        model=cumpany
        fields=[
            'company_name',
            'company_logo',
            'company_city'
        ]