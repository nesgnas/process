from openbabel import openbabel as ob

urlIn  = r'check/compound.pdb'
urlOut = r'check/compound.pdbqt'

#converter  
def converter(infile, outfile,typeIn,typeOut):
  conv = ob.OBConversion()
  conv.SetInAndOutFormats(typeIn, typeOut)
  mol = ob.OBMol()
  conv.ReadFile(mol, infile)
  conv.WriteFile(mol, outfile)

converter(urlIn,urlOut,'pdb','pdbqt')