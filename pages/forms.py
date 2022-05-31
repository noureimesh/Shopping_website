from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your username'
                                , max_length=40,min_length=5)
    password = forms.CharField(label='Your password'
                                , widget=forms.PasswordInput()
                                , max_length=20, min_length=5)
