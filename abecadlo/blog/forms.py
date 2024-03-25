from django import forms
from .models import Post
import datetime
from .Utilities import CIRconvert, smile_check


class Suma(forms.Form):
    pole_nazwa = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':40, 'maxlength':400}))
    pole_smiles = forms.CharField(required = False,widget=forms.TextInput(attrs={'size':40, 'maxlength':400}))
    #data1 = forms.DateField(initial=datetime.date.today,label="Podaj datę",help_text="data obliczeń")
    #URL = forms.URLField()
    #bool = forms.BooleanField()

    def clean(self):
        cleaned_data = super(Suma, self).clean()
        pole_nazwa = cleaned_data.get("pole_nazwa")
        pole_smiles = cleaned_data.get("pole_smiles")
        
        if pole_nazwa == "" and pole_smiles == "":  #brak nazwy i smiles
            self.add_error('pole_nazwa','podaj dane')
        
        if pole_nazwa != "" and pole_smiles == "":  #brak smiles
            if CIRconvert(pole_nazwa)=='Did not work':
                self.add_error('pole_nazwa','smiles nie istnieje')
            else:
                print('Przeszlo')
                pass
        if pole_nazwa == "" and pole_smiles != "":  #brak nazwy
            if smile_check(pole_smiles)=='it dont work':
                self.add_error('pole_smiles','smiles nie istnieje')
            else:
                print('Przeszlo')
                pass
            
        if pole_nazwa != "" and pole_smiles != "":  #podana nazwa i smiles
            self.add_error('pole_nazwa','wszystkie pola wypełnione')
