def make_png_and_mop(smiles):
    import openbabel.pybel
    czasteczka = openbabel.pybel.readstring("smi", smiles)
    czasteczka.write(format="_png2",filename="molecule.png", overwrite=True)
    czasteczka.make3D()
    czasteczka.write(format="mop",filename="molecule.mop",overwrite=True)

def CIRconvert(ids):
  from urllib.request import urlopen
  from urllib.parse import quote
  try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
    
        ans = urlopen(url).read().decode('utf8')
        for line in ans:
            return ans
    except:
        return 'Did not work'
