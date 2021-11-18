#!/usr/bin/env python3
import requests
import re

infile = open("medline.dat", "r")
outfile = open("abstracts.dat", "wb")

for line in infile:
	ID = line
	url = "http://togows.dbcls.jp/entry/ncbi-pubmed/" + ID + "/"
	r = requests.get(url, allow_redirects=True)
	outfile.write(r.content)

# Getting the abstracts in the list
import random
infile = open("abstracts.dat", "r")
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

print(Abstracts)  
