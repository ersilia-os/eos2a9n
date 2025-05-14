# imports
import os
import csv
import sys

from chembl_similarity import read_100_nearest


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))



# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = read_100_nearest(smiles_list)
no_results = []
for i,o in enumerate(outputs):
    if len(o)==0:
        no_results += [smiles_list[i]]
outputs_r2 = read_100_nearest(no_results)

for i,s in enumerate(smiles_list):
    for i2,s2 in enumerate(no_results):
        if s == s2:
            outputs[i] = outputs_r2[i2]

empty_line = [""]*100
outputs_ = []
for o in outputs:
    if not o:
        outputs_ += [empty_line]
    else:
        outputs_ += [o]

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow([f"smiles_{i:02}" for i in range(100)]) # header
    for o in outputs:
        writer.writerow(o)
