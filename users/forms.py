from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile, resume, flyer, company

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image','phone','job','company']

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = resume
        fields = ['resume_file']

class FlyerUpdateForm(forms.ModelForm):
    class Meta:
        model = flyer
        fields = ['file']

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['name','website','passcode','image']
