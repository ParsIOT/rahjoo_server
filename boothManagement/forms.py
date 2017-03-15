from django import forms
from .models import Booth_Owner_Profile
from django.contrib.auth.models import User
from django.contrib.auth import views


class Booth_Details_Form(forms.ModelForm):
	class Meta:
		model = Booth_Owner_Profile
		fields = '__all__'

	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))
	owner = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))
	description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))


class Login_Form(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name')

	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'username'}))
	password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'password', 'type': 'password'}))
