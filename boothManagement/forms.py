from django import forms
from .models import Booth_Details


class Booth_Details_Form(forms.ModelForm):
	class Meta:
		model = Booth_Details
		fields = '__all__'

	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))
	owner = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))
	description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control editable_element', 'disabled': 'true'}))
