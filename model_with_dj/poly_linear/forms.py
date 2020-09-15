from django import forms

class LinearModel(forms.Form):
    year_of_experience=forms.FloatField(min_value=1,max_value=10)