#!/usr/bin/env python3

import re
import string
import random
import math

abs_file= input("Write the name of the file with the abstracts: ")
infile = open(abs_file, "r")
flag = False
Abstracts = list()
Abs = ""

for line in infile:
    End = re.search(r"^[A-Z]+\s+", line)
    if End is not None and Abs != "":
        flag = False
        Abstracts.append(Abs)
        Abs = ""
    if flag:
        line = re.sub("\n", " ", line)
        Abs += line

    Reresult = re.search(r"^AB\s+-\s(.+)", line)
    if Reresult is not None:
        flag = True
        Abs += Reresult.group(1).strip()
infile.close()

outfile = open("cleanAbs.dat", "w")
for ABS in Abstracts:
    outfile.write(ABS + "\n")
outfile.close()
print(len(Abstracts))
n = int(len(Abstracts) / 10)
tenperc_abs = random.sample(Abstracts, n)
#print(len(tenperc_abs))
wcount = dict()
for Abstract in tenperc_abs:
    words = [word.strip(string.punctuation).lower() for word in Abstract.split()]
    for i in words:
        Reresult = re.search(r"([a-z]+(s)?)", i)
        if Reresult is not None and len(Reresult.group(1)) > 2:
            i = Reresult.group(1)
            if i not in wcount:
                wcount[i] = 0
            if i in wcount:
                wcount[i] += 1
#print(sum(wcount.values()))
for w in sorted(wcount, key=wcount.get, reverse=True):
    print(w, wcount[w])
outfile = open("blacklist.dat", "w")
for w in wcount:
    n = (wcount[w] / sum(wcount.values())) * 100
    if n > 0.009:  # Modify this limit when we get the actual range with all the abstracts
        outfile.write(w + "\n")
    else:
        pass
outfile.close()
