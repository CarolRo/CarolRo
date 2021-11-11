#!/usr/bin/env python3
import requests
import re

# 1.

infile = open("medline.dat", "r")
outfile = open("abstracts.dat", "wb")

for line in infile:
	ID = line
	url = "http://togows.dbcls.jp/entry/ncbi-pubmed/" + ID + "/"
	r = requests.get(url, allow_redirects=True)
	outfile.write(r.content)

# 2

import random
infile = open("abstracts.dat", "r")
flag = False
words = ""
wc = 0
for line in infile:
    End = re.search(r"^[A-Z]+\s+", line)
    if End is not None:
        flag = False
    if flag:
        
        words += line.strip()
        wc += len(words)
        
        
    Reresult = re.search(r"^AB\s+-\s(.+)", line)
    if Reresult is not None:
        flag = True
        words += Reresult.group(1)

wc = words.split()
print(len(wc))


