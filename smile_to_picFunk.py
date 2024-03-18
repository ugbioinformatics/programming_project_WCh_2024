def make_png_and_mop(smiles):
    czasteczka = openbabel.pybel.readstring("smi", smiles)
    czasteczka.make3D()
    czasteczka.write(format="_png2",filename="ala.png")
    czasteczka.write(format="mop",filename="ala.mop")
