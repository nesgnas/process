import threading

import pandas as pd
import requests

def name_compound_csv(num_Order):


    # read excel datafile
    f1 = pd.read_csv(
        r'C:\Users\Lenovo\OneDrive - VietNam National University - HCM INTERNATIONAL '
        r'UNIVERSITY\Desktop\process\input\MCElib.csv',
        low_memory=False)

    # take name in data file
    productName = f1['Product Name']

    # idx is index of var want to take
    idx = num_Order

    # show value
    # print(productName[idx])
    return productName[idx]


def download_compound_rcsb(id, count):


    # https://www.rcsb.org/docs/programmatic-access/file-download-services
    url = r'https://files.rcsb.org/download/' + str(id) + '.pdb'

    # https://stackoverflow.com/questions/44699682/how-to-save-a-file-to-a-specific-directory-in-python
    r = requests.get(url)
    with open('from web/' + str(count) + '_' + str(id) + '.pdp', 'wb') as f:
        f.write(r.content)
    f.close()


def readFile():
    f = open(r'input/5i75.pdb')
    print(f.readline())
    f.close()




def search_comp_rcsb(name_compound): #fix link lai sau
    # name_compound = "Agomelatine (L(+)-Tartaric acid)"
    url1 = "https://search.rcsb.org/rcsbsearch/v2/query?json=%7B%22query%22%3A%7B%22type%22%3A%22terminal%22%2C" \
           "%22label%22%3A%22full_text%22%2C%22service%22%3A%22full_text%22%2C%22parameters%22%3A%7B%22value%22%3A%22" \
           "%5C%22"+name_compound+"%5C%22%22%7D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A" \
           "%7B%22paginate%22%3A%7B%22start%22%3A0%2C%22rows%22%3A25%7D%2C%22results_content_type%22%3A%5B" \
           "%22experimental%22%5D%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D" \
           "%5D%2C%22scoring_strategy%22%3A%22combined%22%7D%7D"

    payload = {}
    headers = {}


    requests.status_codes
    response = requests.request("GET", url1, headers=headers, data=payload)
    if (response.status_code != 204) & (response.status_code != 400) :
        #print(response.status_code)
        data = response.json()
        #print(data)
        print(data["result_set"][0]["identifier"])
        # tra ve id protein su sung
        return data["result_set"][0]["identifier"]
    else:
        print()


def take_name_Download(num_Order):
    name_compound = name_compound_csv(num_Order)
    idComp = search_comp_rcsb(name_compound)
    download_compound_rcsb(idComp, num_Order)

def run_process_one(range_Order):
    num_Order = 2606
    while num_Order < range_Order:

            threading.Thread (target=take_name_Download(num_Order), args=(num_Order,)).start()

            num_Order += 1

#run_process_one(4230)
####################
# o process nay dung de tim va tai ve cac file tu du lieu ban dau
#####################################



#takeName(14)
#idComp = searchComp("Vasicine")
#down(idComp, 3412)
