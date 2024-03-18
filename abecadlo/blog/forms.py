from django import forms
from .models import Post
import datetime

class Suma(forms.Form):
    pole_nazwa = forms.CharField(widget=forms.TextInput(attrs={'size':40, 'maxlength':40}))
    pole_smiles = forms.CharField(widget=forms.TextInput(attrs={'size':40, 'maxlength':40}))
    #data1 = forms.DateField(initial=datetime.date.today,label="Podaj datę",help_text="data obliczeń")
    #URL = forms.URLField()
    #bool = forms.BooleanField()
