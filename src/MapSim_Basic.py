import sys
import pickle
import numpy as np
import os
import re
import string
from constants import *

REF_SEQS="../data/sequences/random/"
REF_MAPS="../data/maps/random/"

def match(Y,templates={}):
	for fsa in templates.keys():
		if fsa.match(Y):
			return True,templates[fsa];
	return False,0


'''

Checks for exact match of an alu

'''

def make_insilico_map(alu, seq):
	molecLen = len(seq)
	fsa = re.compile(alu)
	sites = [(0,0)]
	cutsites = fsa.finditer(seq)# in case we need them later. 
	for cutsite in fsa.finditer(seq):
		sites.append((cutsite.start(),cutsite.end()))
	nanomap = []
	for i in range(len(sites)-1):
		nanomap.append(sites[i+1][0]-sites[i][1])
	return nanomap

def main():
	np.random.seed(1234)
	mer_sizes = np.arange(MIN_K,MAX_K,STEP)
	alus = []
	for k in mer_sizes:
		alu=''.join(np.random.choice(['A','T','C','G'],k))
		alu_writer = open("../data/alu_seq_k.txt","w") # save_alu
		alu_writer.write(alu)
		alu_writer.close()
		alus.append(alu)
		

	
	
	label_map={250:'250bp/',1000:'1kb/', 1*10**5:'100kb/', 2*10**5: '200kb/', 3*10**5:'300kb/', 5*10**5:'500kb/', 10**6 : '1Mb/'}
	genome_sizes = [250,1000, 1*10**5, 2*10**5, 5*10**5, 10**6]
	
	for gsize in genome_sizes:
		print("Processing Genomes of Length "+str(label_map[gsize]))
		for alu in alus:
			i=0
			print("Alu of length " + str(len(alu)))
		
			ref_seqs = [seq for seq in os.listdir(REF_SEQS+str(label_map[gsize])) if not seq.startswith(".")]
			for seq in ref_seqs:
				ref_file = open(REF_SEQS+str(label_map[gsize])+seq,"r")
				sequence = ref_file.readline()
				sequence= sequence.replace("\n","")
				ref_file.close()
				nanomap= make_insilico_map(alu,sequence)
				i=i+1
				if i %100==0:
					print(i)
				pickle.dump(nanomap,open(REF_MAPS+str(label_map[gsize])+str(len(alu))+"_map_for_random_genome_"+str(int(re.search(r'\d+', seq).group()))+".p","wb"))
	
if __name__ == '__main__':
	main()