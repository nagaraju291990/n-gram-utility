#script to generate n grams from a given input file
from argparse import ArgumentParser
import re
import os
import sys
import string
from collections import Counter

def find_n_gram(line, noOfGrams):
	words = line.split(" ") 
	for i, word in words:
		print(i,counter)

parser = ArgumentParser(description='Extract n grams from input file/directory \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + "-n=1|2|3|4|...."
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-n", "--ngrams", dest="ngrams",
					help="provide number of grams to be generated", required=True)
parser.add_argument("-p", "--punc", dest="punc",
					help="specify Y|y for yes or N|n for no for to include or exclude punctuations, default=yes", required=False)

args = parser.parse_args()

inputfile = args.inputfile
noOfGrams = int(args.ngrams)
punc = args.punc

if(punc == None):
	punc = 'y'
else:
	punc = punc.lower()

#print(punc)
#exit()

#print(inputfile)
#print(noOfGrams)

with open(inputfile, "r") as fp:
	lines = fp.readlines()


n_gram_frequency = Counter()

for line in lines:

	#normalize/clean text
	line = line.lower()
	line = re.sub(r'\u00A0'," ",line,flags=re.MULTILINE)
	line = re.sub(r'^ *',"",line,flags=re.MULTILINE)
	line = re.sub(r' *$',"",line,flags=re.MULTILINE)
	line = re.sub(r' +', " ",line,flags=re.MULTILINE)
	line = re.sub(r'\n',"", line, flags=re.MULTILINE)

	#remove punctuations
	if(punc == "y"):
		line = re.sub(r'[^\w\s]', '', line)
	
	text = line.split(" ")
	#print(line, len(text))
	j = 0
	k = noOfGrams
	for i in range(len(text)-noOfGrams+1):
		ngram = ''
		#print(text)
		ngram = text[j:k] 
		k = k+1
		j = j + 1
		#print(i,k,j, ngram)
		ngram_str = ' '.join(ngram)

		n_gram_frequency[ngram_str]+=1

	#print("Iam", line)
#print(n_gram_frequency)

for grams, frequency in n_gram_frequency.most_common():#items():
    print(grams, frequency, sep="\t")