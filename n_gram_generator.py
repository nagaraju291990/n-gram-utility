#script to generate n grams from a given input file
from argparse import ArgumentParser
import re
import os
import sys
import string
from collections import Counter
#import string

def find_n_gram(line, noOfGrams):
	words = line.split(" ")
	for i, word in words:
		print(i,counter)

parser = ArgumentParser(description='Extract n grams from input file/directory \n\r'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie" + " -n=1|2|3|4|...."
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
parser.add_argument("-n", "--ngrams", dest="ngrams",
					help="provide number of grams to be generated", required=True)
parser.add_argument("-p", "--punc", dest="punc",
					help="specify Y|y for yes to exclude punctuation or N|n for no to include punctuation, default=yes", required=False)
parser.add_argument("-f", "--func", dest="func",
					help="specify Y|y for yes to exclude function words or N|n for no to include function words from fw.txt, default=yes", required=False)

args = parser.parse_args()

inputfile = args.inputfile
noOfGrams = int(args.ngrams)
punc = args.punc
func = args.func

if(punc == None):
	punc = 'y'
else:
	punc = punc.lower()

if(func == None):
	func = 'n'
else:
	func = func.lower()

#print(punc)
#print(func)
#print(inputfile)
#print(noOfGrams)
fw_dict = {}
if(func == "y"):
	fp = open("fw.txt", "r")
	fws = fp.read().split("\n")
	fp.close()
	for fw in fws:
		fw_dict[fw] = 1


#with open(inputfile, "r", encoding='utf-8') as fp:
	#lines = fp.readlines()

fp2 = open(inputfile, "r",  encoding='utf-8')
lines = fp2.read().split("\n")
fp2.close()

n_gram_frequency = Counter()

for line in lines:


	line = re.sub(r'\u00A0'," ",line, flags=re.MULTILINE)
	line = re.sub(r'\u2018', "\'", line, flags=re.MULTILINE)
	line = re.sub(r'\u2019', "\'", line, flags=re.MULTILINE)
	line = re.sub(r'\u201C', "\"", line, flags=re.MULTILINE)
	line = re.sub(r'\u201D', "\"", line, flags=re.MULTILINE)
	line = re.sub(r'\u2013', "-", line, flags=re.MULTILINE)
	line = re.sub(r'\u2014', "-", line, flags=re.MULTILINE)
	line = re.sub(r'\ufeff', " ", line, flags=re.MULTILINE)

	#remove punctuations

	if(punc == "y"):
		#line = re.sub(u'[^\s\u0C00-\u0C7F]', '', line, flags=re.UNICODE)
		#print(string.punctuation)
		line = line.strip(string.punctuation)
		line = re.sub(r'[!\"#$%&\'()*+,-\./:;<=>\?@\[\]\^_\`\{|\}\~]', ' ', line, flags=re.MULTILINE)
		line = re.sub(r'[\u06D4\u061F\u060C]', ' ', line, flags=re.MULTILINE)
		#line = re.sub(r'^\W+', '', line, flags=re.UNICODE)

	#normalize/clean text
	#line = line.lower()
	line = re.sub(r'^ *',"",line,flags=re.MULTILINE)
	line = re.sub(r' *$',"",line,flags=re.MULTILINE)
	line = re.sub(r' +', " ",line,flags=re.MULTILINE)
	line = re.sub(r'\n',"", line, flags=re.MULTILINE)



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
	if(func == "y"):
		if(re.search(r'',grams,re.IGNORECASE)):
			sgrams = grams.split()
			flag = 0
			for sgram in sgrams:
				if(sgram in fw_dict):
					flag = 1
			if(flag == 0):
				print(grams, frequency, sep="\t")
	else:
		print(grams, frequency, sep="\t")
