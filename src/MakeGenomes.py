import sys
import numpy as np 
from constants import *
def make_random_genomes(L,n=10,DNA_alph=['A','T','C','G'],outfile="../data/sequences/random/"):
    # makes n genomes of length L. 
    if L<=0:
        print('error, L too small')
        sys.exit(0)
    for j in range(n):
        strand = ''.join(np.random.choice(DNA_alph, L))
        f=open(outfile+"random_genome"+str(j+1)+".txt","w")
        f.write(strand)
        f.close()
       



def make_genomes_from_source(srcFile = '../data/',outfile="../data/sequences/from_source/"):
	'''
	Todo: write this so it takes in a file with a sequence '''
	pass

def main():
    L = 3*10**5
    genome_sizes = [250,1000, 1*10**5, 2*10**5, 3*10**5, 5*10**5, 10**6]
    label_map={250:'250bp/',1000:'1kb/', 1*10**5:'100kb/', 2*10**5: '200kb/', 3*10**5:'300kb/', 5*10**5:'500kb/', 10**6 : '1Mb/'}
    genome_sizes = [250,1000, 1*10**5, 2*10**5, 5*10**5, 10**6]

    for gsize in genome_sizes:
       print("making " + str(NUM_RAND) + " random genomes of length "+str(gsize/10**3)+" kbp")
       make_random_genomes(gsize,NUM_RAND,outfile ="../data/sequences/random/"+str(label_map[gsize]))


if __name__ == '__main__':
	main()
