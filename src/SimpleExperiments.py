##
#
#	Experiment Drivers
#

# 		author: James Bannon
###


import sys
import pickle
import pandas as pd
import numpy as np
import os
import time
import re
from nanzam_utils import *
from Nanzam import *
import matplotlib.pyplot as plt


def plot_x_vs_y(x,ys,fig_ext,title,labs=["none"],xlab="Alphabet Size",ylab="Percentage Correct"):

	ax = plt.subplot(111)
	

	# Hide the right and top spines
	for i in range(len(ys)):

		y=ys[i]
		l = labs[i]
		ax.plot(x, y,label=l)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	plt.legend(loc='right')
	plt.xlabel("Alphabet Size")
	plt.ylabel("Percentage Correct")
	plt.yticks(np.arange(0,101,5))
	plt.savefig("../figs/"+fig_ext+".pdf")
	plt.title(title)
	plt.close()

def compute_score(n_samples, n_correct, n_wrong, n_uncallable,mode=False):
	
	if mode:
		print(n_uncallable)
		return ((1.0*n_correct)/(n_samples-n_uncallable))*100
	else:
		return ((1.0*n_correct)/n_samples)*100
	


def simulated_data_experiment(data_path="../data/maps/random/"):
	#print(hash('LXSMLSL',7,13))

	#sys.exit(0)

	label_map={250:'250bp/',1000:'1kb/', 1*10**5:'100kb/', 2*10**5: '200kb/', 3*10**5:'300kb/', 5*10**5:'500kb/', 10**6 : '1Mb/'}
	genome_sizes = [250,1000, 1*10**5, 2*10**5, 3*10**5,5*10**5, 10**6]
	#genome_sizes = [250,1000, 3*10**5,5*10**5, 10**6]
	mer_sizes = np.arange(MIN_K,MAX_K,STEP)
	print(mer_sizes)
	print(mer_sizes)
	
	mer_sizes=[7]
	

	gsize_percentages=[]
	labels=[]
	for size in mer_sizes:
		for gsize in genome_sizes:
			labels.append(label_map[gsize][:-1])
			maps = sorted([f for f in os.listdir(data_path+str(label_map[gsize])) if not f.startswith(".")]) # don't open system files
			#print(len(maps))
			limited_maps = [i for i in maps if i.startswith(str(size)+"_")]
			#print(limited_maps)

			#print(len(limited_maps))
			#print(str(size)+"_")
			alphabet_sizes= np.arange(2,30)
			percent_correct= []
			for alsize in alphabet_sizes:
				num_samples = len(limited_maps)
				num_correct, num_uncallable, num_wrong = 0,0,0
				num_options, num_options_correct, num_options_wrong =0,0,0
				#print("\n")
				#print("alphabet of size: "+str(alsize))
				#print("\n")
				print("../data/maps/random/"+str(label_map[gsize]))
				#sys.exit(0)
				HT=run_offline_phase(als=alsize,map_dir="../data/maps/random/"+str(label_map[gsize]),prefix=size)
				for mf in limited_maps:
					patient_map = pickle.load(open("../data/maps/random/"+str(label_map[gsize])+mf,"rb"))
					map_id = "Genome_"+str(int(re.search(r'\d+', mf[2:]).group()))
					#print("cell should have "+str(map_id))
					called, sentinel = run_online_phase(patient_map,als=alsize)
					if sentinel==-1:
						num_uncallable+=1
						num_wrong+=1
					elif sentinel==0:
						if map_id==called:
							num_correct+=1
						else:
							num_wrong+=1
					else:
						num_options+=1
						if len(called)>3:
							if map_id == called[0]:
								num_correct+=1
								num_options_correct+=1
							else:
								#print(len(called))
								num_wrong+=1
								num_options_wrong+=1
						else:
							if map_id in called:
								num_correct+=1
								num_options_correct+=1
							else:
								num_wrong+=1
								num_options_wrong+=1
				score= compute_score(num_samples,num_correct,num_wrong, num_uncallable)
				percent_correct.append(score)
				print("Algorithm Called "+str(score)+ " percent of the callable instances correctly.")
				print(str(num_uncallable)+" samples were considered uncallable.")
				print(str(num_options)+" of the samples had more than one choice at calling time.")
				#print("Of these "+ str((num_options_correct/num_options)*100.0) + " were called correctly.")
				print("\n")
			print(num_correct,num_uncallable,num_wrong)
			print("number with collisions: "+str(num_options))
			gsize_percentages.append(percent_correct)
		plot_x_vs_y(alphabet_sizes,gsize_percentages,labs=labels,fig_ext="AlphSize_sgrna_size_"+str(size),title="Performance vs. Alphabet Size for sgrna Size"+str(size))





def main():
	simulated_data_experiment()
if __name__ == '__main__':
	main()