def make_png_and_mop(smiles, id):
    import openbabel.pybel
    import os
    from django.conf import settings
    czasteczka = openbabel.pybel.readstring("smi", smiles)
    os.mkdir(settings.MEDIA_ROOT+'/'+str(id))
    czasteczka.write(format="_png2",filename=settings.MEDIA_ROOT+'/'+str(id)+"/molecule.png", overwrite=True)
    czasteczka.make3D()
    czasteczka.write(format="mop",filename=settings.MEDIA_ROOT+'/'+str(id)+"/molecule.mop",overwrite=True)
    czasteczka.write(format="mol2",filename=settings.MEDIA_ROOT+'/'+str(id)+"/start.mol2",overwrite=True)

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
