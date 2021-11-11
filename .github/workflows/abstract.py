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
