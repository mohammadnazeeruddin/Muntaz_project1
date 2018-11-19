from django.shortcuts import render

from django import forms

class create_form(forms.ModelForm):
	username = forms.CharField(max_length=100)
	message = forms.CharField(max_length=1000)
	