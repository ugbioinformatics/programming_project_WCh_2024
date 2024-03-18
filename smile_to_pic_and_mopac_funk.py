def make_png_and_mop(smiles):
    czasteczka = openbabel.pybel.readstring("smi", smiles)
    czasteczka.write(format="_png2",filename="molecule.png", overwrite=True)
    czasteczka.make3D()
    czasteczka.write(format="mop",filename="molecule.mop",overwrite=True)
