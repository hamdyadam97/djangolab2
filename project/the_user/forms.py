from django import forms


class RegisterFrom(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput())
    email = forms.EmailField(max_length=50,widget=forms.EmailInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput())
