import time
import urllib
import requests
from bs4 import BeautifulSoup

def read_100_nearest(smiles, retries=3, timeout=30):
    data = []

    for input_smiles in smiles:
        input_smiles = input_smiles.strip()
        url_encoded_smiles = urllib.parse.quote(input_smiles)
        url = (
            "https://multi-fpb.gdb.tools/chemblsFP.v1.NoJava/search.jsp"
            "?maxCount=100&type=numOfMols&maxDist=50&group2=None&sdfMol=&inputMol="
            f"&mask=0&smi={url_encoded_smiles}&searchMode=searchByNum&limit=100"
        )

        smiles_list = []
        last_err = None

        for attempt in range(1, retries + 1):
            try:
                r = requests.get(url, timeout=timeout)
                r.raise_for_status()

                soup = BeautifulSoup(r.text, "html.parser")
                results = soup.find_all("textarea")

                T = str(results[0]).splitlines() if results else []
                T = [i for i in T if "CHEMBL" in i]

                smiles_list = [i.split(" CHEMBL")[0] for i in T if i.strip()]

                if smiles_list:  
                    break

            except Exception as e:
                last_err = e

            if attempt < retries:
                time.sleep(2 ** (attempt - 1))

        if not smiles_list and last_err is not None:
            print(f"[WARN] Empty after {retries} tries for {input_smiles}: {last_err}")
        elif not smiles_list:
            print(f"[WARN] Empty after {retries} tries for {input_smiles}")

        data.append(smiles_list)

        time.sleep(10)

    return data
