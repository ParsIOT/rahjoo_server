from django import forms
from .models import Booth_Owner
from django.contrib.auth.models import User


class Booth_Owner_Profile(forms.ModelForm):
	class Meta:
		model = Booth_Owner
		fields = ['firstName', 'lastName', 'email', 'company', 'description', 'boothName', 'phone']

	def __init__(self, user, *args, **kwargs):
		self.user = user
		self.request = kwargs.pop('request', None)
		super(Booth_Owner_Profile, self).__init__(*args, **kwargs)

	firstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	lastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
	boothName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
	company = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class': 'form-control '}))
	description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6'}))

	def clean(self):
		super(Booth_Owner_Profile, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		u = super(Booth_Owner_Profile, self).save(commit=False)
		u.user.first_name = self.cleaned_data.get('firstName')
		u.user.last_name = self.cleaned_data.get('lastName')
		u.user.email = self.cleaned_data.get('email')
		u.company = self.cleaned_data.get('company', '')
		u.boothName = self.cleaned_data.get('boothName', '')
		u.phone = self.cleaned_data.get('phone', '')
		u.description = self.cleaned_data.get('description', '')
		u.user.save()
		u.save()
		return u