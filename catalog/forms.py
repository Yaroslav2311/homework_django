
from django import forms


class Triangle(forms.Form):
    leg1 = forms.IntegerField(label='enter the length of the first leg', min_value=1)
    leg2 = forms.IntegerField(label='enter the length of the second leg', min_value=1)

# class Person(forms.Form):
#     first_name = forms.CharField(required=True, max_length=150)
#     last_name = forms.CharField(required=True, max_length=150)
#     email = forms.EmailField(required=True)
