#!/usr/bin/env python3

import re
import string 
import random

# 1.
"""
infile = open("medline.dat", "r")
outfile = open("abstracts.dat", "wb")

for line in infile:
	ID = line
	url = "http://togows.dbcls.jp/entry/ncbi-pubmed/" + ID + "/"
	r = requests.get(url, allow_redirects=True)
	outfile.write(r.content)

outfile.close()


# 2



infile = open("abstracts1.dat", "r")
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
n = int(len(Abstracts)/10)
tenperc_abs = random.sample(Abstracts, n)


print(len(tenperc_abs))
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

print(sum(wcount.values()))
for w in sorted(wcount, key=wcount.get, reverse=True):
    print(w, wcount[w])




outfile = open("blacklist.dat", "w")

for w in wcount:
    n = (wcount[w] / sum(wcount.values())) * 100 
    if n > 0.009: # Modify this limit when we get the actual range with all the abstracts
        outfile.write(w + "\n")
    else:
        pass

outfile.close()


"""
# 3.

infile = open("blacklist.dat", "r")
infile2 = open("cleanAbs.dat", "r")


blacklist = list()
for line in infile:
    blacklist.append(line[:-1])


relevant_words = list()
for line in infile2:
    words = [word.strip(string.punctuation).lower() for word in line.split()]
    auls = list()
    for w in words:
        Reresult = re.search(r"([a-z]+(s)?)", w)
        
        if Reresult is not None and len(Reresult.group(1)) > 2:   
            if w not in blacklist:
                auls.append(w)

            else:
                pass
    relevant_words.append(auls)

# Paring words and counting them
pairs = dict()
for row in relevant_words:
    for item in range(len(row)):
        for i in range(item + 1, len(row)):
            if (row[item],row[i]) in pairs:
                pairs[row[item],row[i]] += 1
                
            else:
                pairs[row[item],row[i]] = 0 
                

print(pairs)