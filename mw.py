#!/usr/bin/python3
"""
Simple script to generate a plot of a hydrophobicity moving window for 
a sequence (here human rhodopsin)
"""

# Initialize the hydrophobicity dictionary
hphob = {}
hphob['I'] =  00.730
hphob['F'] =  00.610
hphob['V'] =  00.540
hphob['L'] =  00.530
hphob['W'] =  00.370
hphob['M'] =  00.260
hphob['A'] =  00.250
hphob['G'] =  00.160
hphob['C'] =  00.040
hphob['Y'] =  00.020
hphob['P'] =  -0.070
hphob['T'] =  -0.180
hphob['S'] =  -0.260
hphob['H'] =  -0.400
hphob['E'] =  -0.620
hphob['N'] =  -0.640
hphob['Q'] =  -0.690
hphob['D'] =  -0.720
hphob['K'] =  -1.100
hphob['R'] =  -1.800

# Initialize the sequence
seq = "MNGTEGPNFYVPFSNATGVVRSPFEYPQYYLAEPWQFSMLAAYMFLLIVLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVLGGFTSTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLAGWSRYIPEGLQCSCGIDYYTLKPEVNNESFVIYMFVVHFTIPMIIIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWVPYASVAFYIFTHQGSNFGPIFMTIPAFFAKSAAIYNPVIYIMMNKQFRNCMLTTICCGKNPLGDDEASATVSKTETSQVAPA"

# Set the window size
window     = 21

# Sequence length and counter for output of each window
seq_length = len(seq)
count      = 1

# Step through the sequence up to window less than the length
for pos in range(0, seq_length-window):
    score   = 0
    # Grab the window
    sub_seq = seq[pos:pos+window]
    # Step throught the window adding hydrophobicity scores
    for i in range(0, window):
        score = score + hphob[sub_seq[i:i+1]]
    # Calculate the average
    score = score / window
    # Print the result
    print (count, score)
    count = count+1
