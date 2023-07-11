from django import forms
from django.contrib.auth.models import User
from main.models import Profile
from django.contrib.auth.forms import UserCreationForm
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model=User
        fields = ['first_name','last_name','username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']