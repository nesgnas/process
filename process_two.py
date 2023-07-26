import os
from os import path
def takeOutFile(num):
    path_to_directory = r'./from web'
    for f in os.listdir(path_to_directory):
        name = path.basename(f)
        x = name.split("_")
        while x[0] == str(num):
            # print(x)

            return name

def workPubCHem(file):
    url = r'./from web/'+file
    f = open(url,'r')
    for line in f:
        if (line.split(" ")[0]) == 'HETNAM':
            return True

    return False


def fetchPubCHem(file):
    if file != None:
        url = r'./from web/'+str(file)
        print("done")
        f = open(url,'r')
        for line in f:
            print(line)

def wF_fail_test(name):
    f = open(r"./notfound/fail_first_test.txt", "a+")
    f.writelines(str(name)+'\n')
    f.close


for t in range(4200):
    name = takeOutFile(t)
    temp = workPubCHem(name)
    if temp != True:
        wF_fail_test(t)
