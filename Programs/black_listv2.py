
import re
import string
import random
import math
import sys



if len(sys.argv) == 1:      # No commandline arguments
    abs_file = input("Write the name of the file with the downloaded data: ")
elif len(sys.argv) == 2:    # Something is there
    abs_file = sys.argv[1]
else:
    sys.stderr.write("Usage: blacklist_filter.py <file> \n")
    sys.exit(1)


try:
	infile = open(abs_file, "r")

	(flag, Abs) = (False, "")
	Abstracts = list()
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

	outfile = open("Abstracts.dat", "w")
	for ABS in Abstracts:
	    outfile.write(ABS + "\n")


	outfile.close()
except IOError as error:
    sys.stderr.write("Could not open/read the file due to: " + str(error) + "\n")
    sys.exit()	


try:
	n = int(len(Abstracts) / 10)
	sample_abs = random.sample(Abstracts, n)

	wcount = dict()
	if sample_abs == []:
		raise Exception ("Data set is not big enough to efficiently use the program.")
		

	for Abstract in sample_abs:
		words = [word.strip(string.punctuation).lower() for word in Abstract.split()]
		for w in words:

			Reresult = re.search(r"([a-z]+(s)?)", w)
			if Reresult is not None and len(Reresult.group(1)) > 2:
				w = Reresult.group(1)
				if w not in wcount:
					wcount[w] = 0
				if w in wcount:
					wcount[w] += 1

	print(len(sample_abs))
	outfile = open("blacklist.dat", "w")
	for w in wcount:
	    n = (wcount[w] / sum(wcount.values())) * 100
	    print(n)
	    if len(sample_abs) > 500 and n > 0.009:  
	        outfile.write(w + "\n")
	    elif len(sample_abs) < 500 and n > 0.04:
	    	outfile.write(w + "\n")
	    else:
	        pass
	outfile.close()
except Exception as error:
	print("The exception is:", str(error))
