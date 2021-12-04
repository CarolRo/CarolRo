# Project: "Text mining MEDLINE abstracts"

##Introduction:
The paper production in Science and Technology over time has surged exponentially in fields such as physics, biology, chemistry, Mathematics, Clinical Medicine, Biomedical Research, Engineering, and technology (Fire and Guestrin., 2019) Figure 1. This massive production of Scientific papers is slow to process, read and filter manually for practical uses, but mining is a good strategy to optimize it. Data mining is a process to discover patterns in a large data set and extract data. Current text mining supports abstract screening, comparing phrases, counting words, and extracting key information. In order to filter non informative words, the word count is used to discard the most abundant words in a group of text; those words are very common in certain fields. The words that are not very common can be used to count the co-occurrence of different pair word combinations in the abstracts. This co-occurrence will show how associated the papers are according to those pair-words. The number of pairings grows geometrically while the occurrence of all the pairings is sparse, the pair counting is fundamental due that some combination words are not very common to find. These counts could be summarized in a matrix, this co-occurrence matrix allows to define of a weighted graph and direct graph. For example, using two phrases: 1) With fear and filth and cowardice and shame, 2) Yes and lover, lover, lover, lover, lover, lover, lover come back to me. Using these sentences we can count the pair co-occurrence shown as the weights of the edges considering the links between all the lexical forms (Figure 2).


Increasing the sentences or number of words increases the amount of combination for the co-occurrence, those combinations could show association or not. The association could be determined by the log ratio of observed co-occurrence using the log-likelihood (LLH) score for the word par; if the pair LLH value >0 it means the pair is over-represented and therefore associated.
In the present study, a set of 20,000 abstracts as a result of the search “Metagenomics' ' in NCBI were used. Metagenomics is defined as the study of genomes recovery from environmental samples which contain information of a mixed community of microorganisms. This field has increased as a result of the decreasing price of the sequencing since the first publication in 1996 to 2021 with 24,664 results in PubMed. Here we present data mining based on the frequency of words and co-occurrence of pair words to estimate the overrepresentation of words within an abstract in Metagenomics.

# Theory

Considerations
1-The abstracts have a different number of words on average between 300-400 words.
2-Contain numbers and special characters.
3-Could find the same word in plural.
4-The papers even from the same field Metagenomics could carry specialized or unique words 

Deliberations
1-The program will be able to work with abstracts with different number of words 
2-Will count the words in each abstract 
3- Due to consideration 4 a random selection of 10% of the abstracts will be used to create a black list that contains the words with the highest number of occurrences in all of them. 
4- This black list will be used to remove the words from the whole set of abstracts and create a clean abstract with less repetitive words. 
5-The comparison of the co-occurrence pair words will be within the abstract.

# Algorithm Design
Detailed Algorithm
Using an ID list, download the paper information from PubMED
            	extract only the abstracts information 
Create the black list with the most abundant words  in the 10% of the abstract
	remove those words in all the abstracts
Calculate the co-ocurrence of pair words 
	apply the LLH 


# Program Design: 
To provide better flexibility to the user and the data that will be used, we designed three programs that can be piped, allowing a higher control of input and output for each program (Figure 3).
The first one consists of a loop that will read the IDs provided in a file and download the corresponding MEDLINE information using the requests library.

The second program consists of a first parsing of the downloaded data that will clean all the background noise leaving just the abstracts this is achieved by studying the downloaded data and assigning flags to relevant information in this case “AB” will notify the start of the abstracts and any new line that starts with two uppercase letter ends the reading. When all the file has been parsed the clean abstracts will be saved in a new file for better observation or future studies. At the same time a random sampling of 10% of the total number of abstracts will be created, from this sample, the program extracts the words by removing any sign of punctuation (using string.punctuation) and any other possible element that is not a word char, this words as long as they are longer than one single character (this decision was made based on the assumption that single letter words or non-words only contribute to background noise and do not need to be taken into consideration) will be counted and evaluated based on its occurrence, the limits were set based on the number of abstracts used for the blacklist, for an abstract dataset higher than 500 only words with an occurrence higher than 0.009 will be added to the blacklist, while with datasets lower than 500 the limit was set to 0.04.

The third and last, the program will ask for a blacklist and a file with abstracts. First, the program will create a list containing all the blacklisted words, then it will extract all the words from the abstracts and save them in a dictionary as long as they are not on the blacklist. The resulting dictionary will contain a nested dictionary in which the first key will be the complete abstract and the value will be the nested dict (with the "informative" words). The next step of the program will be to create two new dicts, one for the co-occurrence tables and one for the log-likelihood (LLH). Both of them iterate through the abstracts(keys of the first dict) and through the word occurrence(value of the first dict). The program will compare the values of occurrence of all the words contained in an abstract and will assign the lowest value to the co-occurrence value ( Because if one word has an occurrence of 1, its co-occurrence with other words can only be one), the values will be stored in the dict. For the LLH we will do a logarithm of the co-occurrence value divided by the number of words in each abstract.
So in the end, we will get the two dicts with 2 nested dicts: the most inner dict will contain the words as keys and the calculated value as value, the second dict will contain the unique words as key an the most inner dict as value, and the outer dict will contain the abstracts as keys and the other dicts as values.
The program also contains user interactions asking for a word and which one of the tables he wishes to consult. The program will then respond with all the data related to that specific word contained in the tables.


# Program Manual: 
The present program could be run in a local computer with a small number of abstract (~1000 suggested) or run in the computerome cluster with a bigger set of abstract (~20,000). In order to download the pubmed information you should provide a list with the IDs that you are interested in (for more information about how to download the IDs read the following page: https://www.terkko.helsinki.fi/files/15948/PubMed_ID_eng.pdf ). This list  should be in a file and one ID per line as the Figure 4 shows. In order to test the program we provide a small set of IDs (probe_IDs.txt).


Local computer: 
In order to download the paper from the list  run the file_downloader.py
./file_downloader.py
OR
python3  file_downloader.py
The output of this program will be a file that contains the paper information (Tittle, author, abstract etc) it is alled abstracts.dat.
Black list creation 
note: before running this program you should verify that you have the  abstracts.dat file (previously created) in the word directory
./black_list.py
OR
python3  black_list.py
The output of this program is a list with the most abundant words that will be used to remove the other abstracts. 

Co-occurrence 
note: before running this program you should verify that you have the blacklist.dat  and cleanAbs.dat files  (previously created) in the word directory.
./co-ocurrence.py
OR
python3  co-ocurrence.py
This program counts the pair co-occurrence words, asks the user for a word of interest and looks in the list for the coincidence and prints if the word was associated with the abstracts. 
Cluster: 
In order to run the analysis in the cluster previously you need to access your account to the computerome server as the guide explains (guide: http://gbar.dtu.dk/faq/53-ssh ). There is a file that contains a list of 20,000 IDs (IDs.txt). The programs are in /zhome/40/9/166068/Python. you can copy to your own directory using cp command. In order to run the programs: 
python3  file_downloader.py
python3  black_list.py
python3  co-ocurrence.py
Github
The programs, the files samples were added to Github in the following link: https://github.com/CarolRo/CarolRo 

# Runtime Analysis: 


| Tables            | Are                                                          |
| ------------------|:------------------------------------------------------------:|
| data_dowloader.py | O(1) + O(1) + O(N) + O(1)                                    | 
| black_list.py     | O(logn) + O(n) + O(n) + O(n) + O(n^2) + O(n) + O(logn) + O(1)|
| co-ocurrence.py   | O(n) + O(1) + O(n) + O(n^2) + O(n^2) + O(n^2) + O(log2n)     |





# Conclusion: 
The present program is able to find co-occurrence and determine if two pair words within the abstract  are associated. A future improvement will be to determine the pair word association in multiple abstracts and make it interactive where the user could introduce a pair of words and see the co-occurrence value in a set of abstract.  Another limitation of this program is the abbreviation of different words or even the gene names. In a future version it could be removed from the abstracts, probably using a set that contains abbreviations in the field or name of genes. 


