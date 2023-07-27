import os
from os import path
def get_fileName(num_Order):
    path_to_directory = r'./from web'
    for f in os.listdir(path_to_directory):
        name = path.basename(f)
        x = name.split("_")
        while x[0] == str(num_Order):
            # print(x)
            return name

def seperate_useless_file(fileName):
    url = r'./from web/' + fileName
    f = open(url,'r')
    for line in f:
        if (line.split(" ")[0]) == 'HETNAM':
            f.close()
            return True
    f.close()
    return False

def writeFile_fail_test(fileName):
    f = open(r"./notfound/fail_first_test.txt", "a+")
    f.writelines(str(fileName)+'\n')
    f.close


def run_process_two(range_Order): #filled_all_useless_file

    num_Order = 0
    while num_Order< range_Order:
        fileName = get_fileName(num_Order)
        temp = seperate_useless_file(fileName)

        if temp != True:
            writeFile_fail_test(num_Order)
        num_Order +=1

#run_process_two(4230)

######################################
# o process nay thi da loc ra duoc cac file khong tim thay phan co the fetch
#########################################
#run()
