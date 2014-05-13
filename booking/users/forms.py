from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(max_length = 50, required=False)
    lastname = forms.CharField(max_length=50, required=False)
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=30, required=False)#,unique=True)
    password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput)
    birthdate = forms.DateField('Birthdate', required=False)
    
