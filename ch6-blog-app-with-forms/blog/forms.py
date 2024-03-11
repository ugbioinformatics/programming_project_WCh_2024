from django import forms
from .models import Post
import datetime

class Suma(forms.Form):
    body = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'size':40, 'maxlength':40}))
    data1 = forms.DateField(initial=datetime.date.today,label="Podaj datę",help_test="data obliczeń")
