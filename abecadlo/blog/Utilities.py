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


def calculate(post, id):
    import openbabel.pybel
    from django.conf import settings
    import fileinput
    import subprocess

    czasteczka = next(openbabel.pybel.readfile("mopout",settings.MEDIA_ROOT+'/'+str(id)+"/molecule.out"))
    czasteczka.write(format="mop",filename=settings.MEDIA_ROOT+'/'+str(id)+"/force.mop",overwrite=True)
    czasteczka.write(format="mop",filename=settings.MEDIA_ROOT+'/'+str(id)+"/drc.mop",overwrite=True)
    metoda = post.metoda
    with fileinput.FileInput(settings.MEDIA_ROOT+'/'+str(id)+"/force.mop", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('PUT KEYWORDS HERE',f"{metoda} force"), end='')
    subprocess.run(['/opt/mopac/MOPAC2016.exe', 'force.mop'], cwd = settings.MEDIA_ROOT+'/'+str(post.id))
    
    with open(settings.MEDIA_ROOT+'/'+str(id)+"/force.out", 'r') as file:
        nazwa = file.readlines()
        post.calculations = nazwa
        post.save()

    with fileinput.FileInput(settings.MEDIA_ROOT+'/'+str(id)+"/drc.mop", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('PUT KEYWORDS HERE',f"{metoda} irc=1* DRC BIGCYCLES=1 html t-priority=0.5"), end='')

    subprocess.run(['/opt/mopac/MOPAC2016.exe', 'drc.mop'], cwd = settings.MEDIA_ROOT+'/'+str(post.id))

