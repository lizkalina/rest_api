from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=50)
    favorite_city = forms.CharField(max_length=50)
