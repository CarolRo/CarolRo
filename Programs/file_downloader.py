import sys

import requests
try:
    IDs_file= input("Write the name of your file with the pumbmed IDs to dowload: ")
    infile = open(IDs_file, "r")
    outfile = open("abstracts.dat", "wb")
    for line in infile:
	    ID = re.search(r"^(\d+)", line)
	    if ID is not None:
	        url = "http://togows.dbcls.jp/entry/ncbi-pubmed/" + ID.group(1) + "/"
	        r = requests.get(url, allow_redirects=True)
	        outfile.write(r.content)
		
    infile.close()		
    outfile.close()
    print("Your data was downloaded the file is called: abstracts.dat")
except OSError as error:
    sys.stderr.write("Could not open/read file, check if your file exists:", IDs_file, "\n")
    sys.exit()
