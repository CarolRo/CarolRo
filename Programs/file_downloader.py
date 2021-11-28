import sys

import requests
try:
    IDs_file= input("Write the name of your file with the pumbmed IDs to dowload: ")
    infile = open(IDs_file, "r")
    outfile = open("abstracts.dat", "wb")
    for line in infile:
	    ID = line
	    url = "http://togows.dbcls.jp/entry/ncbi-pubmed/" + ID + "/"
	    r = requests.get(url, allow_redirects=True)
	    outfile.write(r.content)
    outfile.close()
    print("Your data was downloaded the file is called: abstracts.dat")
except OSError:
    print ("Could not open/read file, check if your file exist:", IDs_file)
    sys.exit()
