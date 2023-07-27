from process_four import run_process_four
from process_one import name_compound_csv

def run_process_five(range_Order):
    f = open('./notfound/fail_first_test.txt')
    a = f.readlines()
    check = 0
    count =0;
    for num in range(range_Order):

        #print('num is')
        print(num)
        # print(f.readline()+"SOS")
        #print('chek is')
        #print(check)
        #print('acheck')
        #print(a[check])
        if num> int(a[check]):
            check +=1
        else:
            if num == int(a[check]):
                check +=1
                continue
            else:
                print(name_compound_csv(num))
                value = run_process_four(num)
                if value!= None:
                    count +=1
                #print()
    f.close()
    print("FOUNDED")
    print(count)

run_process_five(4230)