import pubchempy as pcp
from process_one import name_compound_csv

def get_iupacName_PubChem(compound):
    # print("****************")
    c = pcp.get_compounds(compound,'name')

    if c != []:

        # print(c[0].iupac_name)
        # print("________________")
        return c[0].iupac_name
    else:
        return None

def checkSingleCompound(cmp):
    c = pcp.get_compounds(cmp,'name')
    print(c[0].iupac_name)

def test():
    for i in range(10):
        get_iupacName_PubChem(name_compound_csv(i))

################################
# o file process 3 nay thi tim dươc iupac name cua hop chat
################################

#mockPubChem(' CHLORIDE ION')
#checkSingleCompound(" 6-[1-(3,5,5,8,8-PENTAMETHYL-5,6,7,8-TETRAHYDRONAPHTHALEN-2-YL)CYCLOPROPYL]PYRIDINE-3-CARBOXYLICACID")
# checkSingleCompound("2-ACETAMIDO-2-DEOXY-BETA-D-GALACTOPYRANOSE")
#checkSingleCompound(" CHLORIDE ION")
#checkSingleCompound(" 6-[1-(3,5,5,8,8-PENTAMETHYL-5,6,7,8-TETRAHYDRONAPHTHALEN-2-YL)CYCLOPROPYL]PYRIDINE-3-CARBOXYLIC ACID")

#mockPubChem(takeName(24))