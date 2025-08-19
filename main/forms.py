from django import forms
from datetime import date

class UsernameForms(forms.Form):
    username = forms.CharField(label="name", max_length=50)

class AddForm(forms.Form):
    value = forms.IntegerField()
    transactionDate = forms.DateField(initial=date.today(), label="Date")
    source = forms.CharField()
    borrowed = forms.BooleanField(required=False)
    toMonthly = forms.BooleanField(label="inlcude in monthly income", initial=True, required=False)
    add10pcent = forms.BooleanField(label="10%", initial=False, required=False)
