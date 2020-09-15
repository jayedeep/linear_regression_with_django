from django import forms

class LinearModel(forms.Form):
    cylinders=forms.IntegerField(max_value=8,min_value=3)
    displacement=forms.IntegerField(max_value=500,min_value=68)
    horsepower=forms.IntegerField(max_value=250,min_value=46)
    weight=forms.IntegerField(max_value=5150,min_value=1613)
    acceleration=forms.IntegerField(max_value=30,min_value=8)
    model_year=forms.IntegerField(max_value=82,min_value=70)
    origin=forms.IntegerField(max_value=3,min_value=1)