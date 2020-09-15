from django import forms

class LinearModel(forms.Form):
    MF=[("male",'male'),('female','female')]
    male_or_female=forms.ChoiceField(widget=forms.RadioSelect,choices=MF)
    height=forms.CharField()
