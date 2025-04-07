import subprocess
import sys
import time

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", bs4])

from bs4 import BeautifulSoup

import requests
import json
import sys
import urllib
from time import sleep


def read_100_nearest(smiles):
    data = []
    for input_smiles in smiles:
        input_smiles = input_smiles.strip() 
        url_encoded_smiles = urllib.parse.quote(input_smiles)
        url = 'https://multi-fpb.gdb.tools/chemblsFP.v1.NoJava/search.jsp?maxCount=100&type=numOfMols&maxDist=50&group2=None&sdfMol=&inputMol=&mask=0&smi=' + url_encoded_smiles + '&searchMode=searchByNum&limit=100'
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features = 'html.parser')
        results = soup.find_all('textarea')
        T = str(results[0]).splitlines() if results else []
        T = [i for i in T if not ('CHEMBL' not in i)]
        smiles_list = []
        for i in T:
            x = i.split(" CHEMBL")[0]
            smiles_list.append(x)
        data+= [smiles_list]
        time.sleep(10)
    return data
