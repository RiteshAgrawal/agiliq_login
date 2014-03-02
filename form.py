from django import forms

class Application(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	projects_url = forms.CharField(max_length=100)
	code_url = forms.CharField(max_length=100)
	resume = forms.FileField()

