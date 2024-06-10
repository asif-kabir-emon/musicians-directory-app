from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(), strip=False)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(), strip=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
        }

class UpdateUserProfileDataForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': None,
            'first_name': None,
            'last_name': None,
            'email': None,
        }