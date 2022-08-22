from bs4 import BeautifulSoup
import requests
import json
import sys

# Input Parameters
input_file = open(sys.argv[1], 'r')
Lines = input_file.readlines()[1:]

data = []
for input_smiles in Lines:
    input_smiles = input_smiles.strip() 
    url = 'http://130.92.106.217:8080/chemblECfp4.v1.NoJava/search.jsp?maxCount=100&type=numOfMols&maxDist=50&group2=None&sdfMol=&inputMol=&mask=0&smi=' + input_smiles + '&searchMode=searchByNum&limit=100'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features = 'html.parser')
    results = soup.find_all('textarea')
    
    T = str(results[0]).splitlines()
    T = [i for i in T if not ('CHEMBL' not in i)]
    smiles_list = []
    similarity_indices = []
    for i in T:
        x = i.split(" CHEMBL")[0]
        x2 = i.split(" ")[2]
        smiles_list.append(x) 
        similarity_indices.append(x2)
        
    data+= [[smiles_list, similarity_indices]]



with open(sys.argv[2], 'w') as f:
    json.dump(data, f)
