from django.core import validators
from django import forms
from .models import User

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'fname', 'lname', 'age', 'email']
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'})
        }
     