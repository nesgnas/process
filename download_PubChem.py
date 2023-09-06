import requests

def take_response_PubChem(order_Num,idC):

  url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/"+str(idC)+"/record/SDF?record_type=3d&amp;response_type=save" \
        "&amp;response_basename=Structure3D_COMPOUND_CID_"+str(idC)+"\""

  payload = {}
  headers = {
    'Cookie': 'ncbi_sid=95B61EB14C5DE401_0000SID'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  url = r'./fromPC/'+str(order_Num)+'.'+str(idC)+'.sdf'
  with open(url, "w") as f:
    f.write(response.text)
  print(response.text)








#take_response_PubChem(1,8853)