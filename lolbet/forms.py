from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(label="Username", max_length=30, required=True)
	email = forms.EmailField(label="Email", required=True)
	password1 = forms.CharField(label="Password", min_length=8, required=True, widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm Password", min_length=8, required=True, widget=forms.PasswordInput)
	verifyAge = forms.DateField(required=True)