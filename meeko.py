import rdkit as rd
import meeko as mk

smile_molecule = '[C@@H]1([C@@H]([C@H]([C@H]([C@@H](CO)O1)O)O)NC(=O)C)O'

lig =  rd.Chem.MolFromSmiles(smile_molecule)
protonated_lig =  rd.Chem.AddHs(lig)
rd.Chem.AllChem.EmbedMolecule(protonated_lig)

meeko_prep = mk.MoleculePreparation()
meeko_prep.prepare(protonated_lig)
lig_pdbqt = meeko_prep.write_pdbqt_string()

v = vina.Vina