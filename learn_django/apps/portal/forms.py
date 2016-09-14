from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    auth = forms.CharField(label='Password')