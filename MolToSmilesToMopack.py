from urllib.request import urlopen
from urllib.parse import quote

from urllib.request import urlopen
from urllib.parse import quote

#Punkt_1
# 2 pola tekstowe z nazwa czasteczki smiles
def clean(self):
    cleaned_data = super(self).clean()
    mol_name = cleaned_data.get("NZAWA CZASTECZKI")
    smile_code = cleaned_data.get("KOD SMILES")
    identifiers = input()

    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles' 
        ans = urlopen(url).read().decode('utf8')
        return ans
    except:
        self.add_error('Blad.')
#        return 'Did not work'

#Punkt_2
# Komunikat, przy enterze, ze pole jest puste

#Punkt_3
# Funkcja do konwersji


#Punkt_4
