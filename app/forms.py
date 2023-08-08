from django import forms
from .models import UserProfile

class Step1Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username']

class Step2Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']

class Step3Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['password']
