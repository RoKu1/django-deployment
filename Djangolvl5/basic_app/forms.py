from django import forms
from django.contrib.auth.models import User
from .models import userprofileinfo



class  UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class UserprofileForm(forms.ModelForm):
    class Meta():
        model = userprofileinfo
        fields = ('profile_link','profile_pic')
