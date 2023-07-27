from process_three import get_iupacName_PubChem
from process_two import get_fileName
from process_one import name_compound_csv

def match_PubChem_and_Rcsb(fileName,num_Order):
    url = r'./from web/' + fileName
    f = open(url, 'r')
    arr = [""]*10   # code of compound
    arr1 = [""]*10
    arr2 = [""]*10
    count=0

    for line in f:
        if (line.split(" ")[0]) == 'HETNAM':
            # print(line.split(" "))
            count +=1
            j = 2
            while line.split(" ")[j] == "":
                j +=1
            if line.split(" ")[j+1] == arr[count-1]:
                count -= 1
                j +=2
                condtion = False
                i = j + 1
                arr1[count] +=line.split(" ")[i]
                i += 1
                if line.split(" ")[i] == line.split(" ")[i + 1]:
                    condtion = True
                while condtion != True:
                    arr1[count] += " " + line.split(" ")[i]
                    i += 1
                    if line.split(" ")[i] == line.split(" ")[i + 1]:
                        condtion = True
            else:
                arr[count] = line.split(" ")[j]  # take code of compound
                # print("___ CODE PROCESS ___")
                # print(arr[count])
                condtion = False
                i = j + 1
                while condtion != True:
                    arr1[count] += " " + line.split(" ")[i]

                    i += 1
                    if line.split(" ")[i] == line.split(" ")[i + 1]:
                        condtion = True
            # print("___ FINAL RESULT ___")
            # print(arr1[count] + '\n')

    # print("___________________")
    for i in range(count+1):
        if i==0:
            continue
        else:
            arr2[i] = get_iupacName_PubChem(arr1[i])

    name_compound = name_compound_csv(num_Order)
    name_compound_PubChem = get_iupacName_PubChem(name_compound)

    for i in range(count+1):
        if name_compound_PubChem == arr2[i]:
            return arr[i]
    return None

def run_process_four(num_Order):    #get_code_founded
    fileName = get_fileName(num_Order)
    value = match_PubChem_and_Rcsb(fileName,num_Order)
    print(value)
    return value
#run_process_four(65)
###################################
# o process nay tim code cua hop chat tu file fetch dc roi tra ve "code" neu TRUE, "NONE" neu FALSE
###################################


# get_code_founded(3)