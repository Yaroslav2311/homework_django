from django import forms
from .models import Person


class Triangle(forms.Form):
    leg1 = forms.IntegerField(label='enter the length of the first leg', min_value=1)
    leg2 = forms.IntegerField(label='enter the length of the second leg', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
