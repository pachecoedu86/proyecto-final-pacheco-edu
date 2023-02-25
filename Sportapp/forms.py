from django import forms


class sportFORMULARIO(forms.Form):
    name = forms.CharField()
    country = forms.CharField()

class playerFORMULARIO(forms.Form):
    name = forms.CharField() 
    surname = forms.CharField()
    age = forms.IntegerField() 


class coachFORMULARIO(forms.Form):
    name = forms.CharField()
    surname= forms.CharField()
    age = forms.IntegerField()
    category = forms.CharField() 

class teamFORMULARIO(forms.Form):
    name = forms.CharField()
    country = forms.CharField()
    host = forms.CharField()
    Championships = forms.IntegerField()

