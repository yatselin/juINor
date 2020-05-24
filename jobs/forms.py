from django import forms
from .models import Company, Application

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location', 'description', 'employee_count', 'logo',)
        required = ("name",)

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'phone', 'cover_letter', )
        required = ("name",)   

 