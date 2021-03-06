from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ins.models import InsUser

# forms defined here handles user inputs

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InsUser
        fields = ('username', 'email', 'profile_pic')