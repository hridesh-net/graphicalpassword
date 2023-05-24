from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password_image = forms.ImageField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password_image', 'password']