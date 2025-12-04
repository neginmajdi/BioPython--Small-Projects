
"""
Cas9 Protein Sequence Analysis
Author: Negin Majdi

This script analyzes the amino acid sequence of the Cas9 protein.
It performs the following steps:

1. Opens a local file containing the Cas9 sequence (cas9-seq.txt).
2. Counts the frequency of each amino acid in the sequence.
3. Computes the hydropathy values to classify amino acids as 
   hydrophobic or hydrophilic.
4. Generates visualizations:
   - A bar chart showing amino acid frequencies.
   - A boxplot comparing hydrophobic vs hydrophilic residues.

The analysis helps to understand the composition and 
hydrophobic/hydrophilic properties of Cas9 at a glance.
"""

import pandas as pd 
import matplotlib.pyplot as plt
from collections import Counter

with open ("cas9-seq.txt", "r") as f:
    seq=list(f.read().strip())

aa_names_standard = {
    'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe',
    'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys', 'L': 'Leu',
    'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg',
    'S': 'Ser', 'T': 'Thr', 'V': 'Val', 'W': 'Trp', 'Y': 'Tyr'
}

Hydropathy = {
 'A': 1.8,  'C': 2.5,  'D': -3.5, 'E': -3.5, 'F': 2.8,
 'G': -0.4, 'H': -3.2, 'I': 4.5,  'K': -3.9, 'L': 3.8,
 'M': 1.9,  'N': -3.5, 'P': -1.6, 'Q': -3.5, 'R': -4.5,
 'S': -0.8, 'T': -0.7, 'V': 4.2,  'W': -0.9, 'Y': -1.3
}

sequence=[]
for aa in seq:
    if aa in aa_names_standard:
        sequence.append(aa)
print("Aminoacides number:", len(sequence))

counts=Counter(sequence)
print("the number of each aa is:")
for aa,n in counts.items():
    print(aa, aa_names_standard[aa], n)

plt.bar(counts.keys(), counts.values())
plt.xlabel("AminoAcid")
plt.ylabel("Frequency")
plt.title("Cas9 AminoAcids")
plt.savefig("aminoacid.png")
plt.show()

hydrophobic=[]
hydrophilic=[]

for aa in sequence:
    if Hydropathy[aa]>=0:
        hydrophobic.append(Hydropathy[aa])
    else:
        hydrophilic.append(Hydropathy[aa])
len(hydrophobic)

plt.boxplot([hydrophobic, hydrophilic])
labels=('Hydrophobic', "Hydrophilic")
plt.ylabel("Hydropathy")
plt.title("Hydropathy of Cas9")
plt.savefig("hydrophobicity.png")
plt.show()