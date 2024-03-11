from django import forms
from .models import Post
import datetime

class Suma(forms.Form):
    body = forms.CharField(label="Dane",help_text="liczby do sumowania",max_length=40,widget=forms.TextInput(attrs={'size':40, 'maxlength':40}))
    data1 = forms.DateField(initial=datetime.date.today,label="Podaj datę",help_text="data obliczeń")
    URL = forms.URLField()
    bool = forms.BooleanField()
    time = forms.TimeField()
    decimal = forms.DecimalField(max_digits = 5, decimal_places = 3)

    def clean(self):
        cleaned_data = super(Suma, self).clean()
        lista=cleaned_data.get("body")
        tmp=lista.split()
        s=0
        for item in tmp:
            try:
                s=s+int(item)
            except:
                self.add_error('body','zła lista')
