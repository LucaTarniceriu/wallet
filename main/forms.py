from django import forms

class UsernameForms(forms.Form):
    username = forms.CharField(label="name", max_length=50)
