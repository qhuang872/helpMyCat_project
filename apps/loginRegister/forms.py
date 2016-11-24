from django import forms
from .models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class RegisterForm(ModelForm):
    class Meta:
        model=User
        fields='__all__'
    def clean(self):
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirmPassword']
        if password != confirm:
            raise ValidationError("password and confirm password do not match")
        return self.cleaned_data

    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    email = forms.EmailField(required=True,label='',widget=forms.EmailInput(attrs={'placeholder':'Enter email'}))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    confirmPassword = forms.CharField(required=True,label='',max_length=255,widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    
class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=('username','password')
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        user = User.objects.get(username=username)
        if user.password != password:
            raise ValidationError("wrong password")
    username = forms.CharField(required=True,label='',widget=forms.TextInput(attrs={'placeholder':'Enter username'}))
    password = forms.CharField(required=True,label='',widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    

