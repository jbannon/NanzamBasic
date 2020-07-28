##
#
#
#	Basic Nanzam
#
####

import sys
import pickle
import pandas as pd
import numpy as np
import os
import re
import time
from constants import *
from nanzam_utils import *
import string

def run_offline_phase(ws = 5,als=8,ts = TABLE_SIZE, D=256,map_dir="../data/maps/random/",prefix=7):
	''' Prefix makes sure it looks in the right direction.  change to focus on directory'''

	maps = sorted([f for f in os.listdir(map_dir) if not f.startswith(".")]) # don't open system files
	maps = [i for i in maps if i.startswith(str(prefix)+"_")]
	Lookup_Table = makeTable(ts)
	lengths, ref_maps = collect_lengths_and_maps(maps,map_dir)
	alphabet,almap, bins = make_Alphabet(np.array(lengths),als)
	translated_maps=[]
	for i in range(len(maps)):
		#print(maps[i])
		map_id = str(int(re.search(r'\d+', maps[i][2:]).group()))
		#print(map_id)
		translated_map = translate(ref_maps[i],almap)
		translated_maps.append(translated_map)
		#print(map_id)
		#Lookup_Table[hash(''.join(translated_map),D,ts)].append(("Genome_"+str(map_id),''.join(translated_map)))
		Lookup_Table[hash(''.join(translated_map),D,ts)].append("Genome_"+str(map_id))

	pickle.dump(Lookup_Table,open("../bins/Lookup_Table.p","wb"))
	pickle.dump(almap,open("../bins/Alphabet_Mapping.p","wb"))

	return Lookup_Table


def run_online_phase(patient_map,ws=5,als=8,ts=TABLE_SIZE,D=256):
	Lookup_Table = pickle.load(open("../bins/Lookup_Table.p","rb"))
	almap = pickle.load(open("../bins/Alphabet_Mapping.p","rb"))
	translated_patient = translate(patient_map,almap)
	results_list = Lookup_Table[hash(''.join(translated_patient),D,ts)]
	result_length_toggle = -1
	if len(results_list)==0:
		result_length_toggle = -1 #indicate a missing entry.
	elif len(results_list)>1:
		result_length_toggle = 1 #  length>1
	else:
		result_length_toggle = 0 # has length 1

	if result_length_toggle==0:
		called_id = results_list[0]
	elif result_length_toggle==1:
		called_id = results_list
	else:
		called_id = "NULL"

	return called_id, result_length_toggle


def main():
	'''print(hash("ABCDEFG"))
	Look = run_offline_phase()
	map_dir="../data/maps/random/"

	maps = sorted([f for f in os.listdir(map_dir) if not f.startswith(".")]) # don't open system files
	p_map = pickle.load(open("../data/maps/random/"+maps[0],"rb"))
	a,b = run_online_phase(p_map)
	print(a,";",b)'''
	table = run_offline_phase(ws = 5,als=30,ts = TABLE_SIZE, D=256,map_dir="../data/maps/random/300kb/")
	#print_table(table)




if __name__ == '__main__':
	main()