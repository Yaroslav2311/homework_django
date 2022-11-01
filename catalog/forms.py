
from django import forms


class Triangle(forms.Form):
    leg1 = forms.IntegerField(label='enter the length of the first leg', min_value=1)
    leg2 = forms.IntegerField(label='enter the length of the second leg', min_value=1)
