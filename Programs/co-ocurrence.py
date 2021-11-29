# 3.
def compare_values(p1, p2):
    if (p1 < p2):
        return p1
    else:
        return p2

try:
    infile = open("blacklist.dat", "r")
    infile2 = open("shortcleanAbs.dat", "r")
   

    blacklist = list()
    for line in infile:
        blacklist.append(line[:-1])

    
    relevant_words = dict()
    for line in infile2:
        words = [word.strip(string.punctuation).lower() for word in line.split()]
        abstract = list()
        for w in words:
            Reresult = re.search(r"([a-z]+(s)?)", w)
            if Reresult is not None and len(Reresult.group(1)) > 2:   
                if w not in blacklist:
                    abstract.append(w)
                else:
                    pass
        relevant_words[line] = abstract


    # Paring words and counting them
    unique_words = dict()
    LLH_abs = dict()
    pairs_abs = dict()
    for row in relevant_words:
        w_count = dict()
        for item in relevant_words[row]:

            if item not in w_count:
                w_count[item] = 1
            else:
                w_count[item] += 1

        unique_words[row] = w_count

        
        pairs_w = dict()
        LLH_w = dict()
        for jk, jv in w_count.items():
            pairs_cooc = dict()
            LLH_cooc = dict()
            for ik, iv in w_count.items():
                pairs_cooc[ik] = compare_values(jv, iv)
                LLH_cooc[ik] = math.log(compare_values(jv,iv)/len(row.split()), 10)
            LLH_w[jk] = LLH_cooc
            pairs_w[jk] = pairs_cooc
        pairs_abs[row] = pairs_w
        LLH_abs[row] = LLH_w
    
    
      
    
    #4. 

    word = input("Enter a word: ").lower()
    while word != "stop":
        for abstract in LLH_abs:
            if word not in LLH_w.keys():
                word = input("That word is not an informative one, try again: ").lower()
            else:
                if LLH_abs[abstract].get(word) is not None:
                    print(word,"appears in:\n",abstract, "\n", "Its LLH with the words in that abstract is: ", LLH_abs[abstract].get(word))
                
        word = input("Enter a new word or write stop. ")
                        
        
        
            
            
            
except IOError as error:
    sys.stderr.write("I/O error, reason: " + str(error) + "\n")
