import sys
import pickle
import pandas as pd
import numpy as np
import os
import time
from constants import *
import string


''' Alphabet and Hashing Tools'''
def hash(merString,D=256,q=101):
	"""
	computes rabin karp fingerprint of the string

	"""
	hashval = 0
	for i in range(len(merString)): # preprocessing
		hashval = (hashval*D+ord(merString[i]))%q
	return hashval


def makeTable(table_size):
	"""
	speeds up so we don't have if checks
	"""
	table = {}
	for k in range(table_size):
		table[k] = []
	return table


def collect_lengths_and_maps(map_file_names,dirname="../data/maps/random/"):
	lengths = []
	reference_maps = []
	for mf in map_file_names:
		current_map = pickle.load(open(dirname+mf,"rb"))
		reference_maps.append(current_map)
		lengths.extend(current_map)
	return lengths, reference_maps


def make_almap(bins):
	print("making alphabet of size "+str(len(bins)))
	if len(bins)<1:
		print("error, length of bins less than one, aborting")
		sys.exit(0)
	elif len(bins)<=9:
		alphabet = SIMPLE_ALPHS[len(bins)-1]
	else:
		lowers = list(string.ascii_lowercase)
		uppers = list(string.ascii_uppercase)
		uppers.extend(lowers)
		alphabet = uppers[0:len(bins)]
	almap = {}
	for dex in range(len(bins)-1):
		range_tup = (bins[dex],bins[dex+1])
		almap[range_tup]=alphabet[dex]
	return alphabet, almap

	
def make_Alphabet(length_array, n_bins,qcut=True):
		"""keep bin static"""

		if qcut:
			cuts = pd.qcut(length_array,n_bins,retbins=True,precision=1,duplicates='drop')
			bins=cuts[1]
			bins = list(np.floor(bins))[1:len(bins)-1]
			if bins[0]!=0:
				bins[0]=0
				
			bins.append(float("inf"))	
		else:
			counts,bins = np.histogram(length_array,n_bins)
			bins = list(bins)[1:len(bins)-1]
			bins.insert(0,float(0))
			bins.append(float("inf"))
		alphabet, almap = make_almap(bins)
		return alphabet,almap,bins


''' Translation Helpers'''

def range_query(y,range_tuple):
	if range_tuple[0]<=y and y<range_tuple[1]:
		return True
	else:
		return False

def range_translate(y,almap):
	for I in almap.keys():
		if range_query(y,I):
			return almap[I]


def translate(length_vector,almap):
	translated_vector = []
	for j in range(len(length_vector)):
		translated_vector.append(range_translate(length_vector[j],almap))
	return translated_vector


def print_table(tab,keys=False):
	if keys:
		for k in tab.keys():
			print(k)
	else:
		for k in tab.keys():
			if tab[k]!=[]:
				print("key: "+str(k))
				print(tab[k])
def print_bin_sizes(tab,average=True):
	if average:
		lens=0
		for k in tab.keys():
			lens+=len(tab[k])
		print(str(lens/len(tab.keys())))
