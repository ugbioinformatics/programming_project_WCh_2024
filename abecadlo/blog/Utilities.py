def make_png_and_mop(smiles, id):
    import openbabel.pybel
    import os
    czasteczka = openbabel.pybel.readstring("smi", smiles)
    os.mkdir(str(id))
    czasteczka.write(format="_png2",filename=str(id)+"/molecule.png", overwrite=True)
    czasteczka.make3D()
    czasteczka.write(format="mop",filename=str(id)+"/molecule.mop",overwrite=True)

def smile_check(smiles):
    import openbabel.pybel
    import os
    try:
        czasteczka = openbabel.pybel.readstring("smi", smiles)
        return 'it work'
    except:
        return 'it dont work'

def CIRconvert(ids):
    from urllib.request import urlopen
    from urllib.parse import quote
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles' 
        print(url)
        return urlopen(url).read().decode('utf8')
    except:
        return 'Did not work'
