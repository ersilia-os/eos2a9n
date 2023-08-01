from bs4 import BeautifulSoup
import requests
import json
import sys

def read_100_nearest(smiles):
    data = []
    for input_smiles in smiles:
        input_smiles = input_smiles.strip() 
        url = 'https://multi-fpb.gdb.tools/chemblsFP.v1.NoJava/search.jsp?maxCount=100&type=numOfMols&maxDist=50&group2=None&sdfMol=&inputMol=&mask=0&smi=' + input_smiles + '&searchMode=searchByNum&limit=100'
        r = requests.get(url)
        print(r)
        soup = BeautifulSoup(r.text, features = 'html.parser')
        results = soup.find_all('textarea')
        print(results)
        T = str(results[0]).splitlines() if results else []
        T = [i for i in T if not ('CHEMBL' not in i)]
        smiles_list = []
        for i in T:
            x = i.split(" CHEMBL")[0]
            smiles_list.append(x)
        data+= [smiles_list]
    return data


