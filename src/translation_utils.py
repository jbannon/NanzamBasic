
import sys
import pickle
import pandas as pd
import numpy as np
import os
import time
from constants import *


def boundary_translate(y,almap,eps):
	res_list =[]
	for dex in range(len(almap.keys())):
		I=list(almap.keys())[dex]
		m,u,l =boundary_query(y,I,eps)
		if m:
			res_list.append(almap[I])
			if u:
				res_list.append(almap[list(almap.keys())[dex+1]])
			elif l:
				res_list.append(almap[list(almap.keys())[dex-1]])
			return res_list


def translate2(length_vector,almap,jitter=True,epsilon=0.01):
	if jitter:
		possible_maps=[]
		for j in range(len(length_vector)):
			new_letters=[x for x in boundary_translate(length_vector[j],almap,epsilon)]
			if len(possible_maps)==0:
				for letter in new_letters:
					possible_maps.append([letter])
			else:
				new_maps=[]
				for possible_map in possible_maps:
					for letter in new_letters:
						temp = [x for x in possible_map]
						temp.append(letter)
						new_maps.append(temp)
				possible_maps=new_maps
		return possible_maps
	else:
		#translate from old code base
		translated_vector = []
		for j in range(len(length_vector)):
			translated_vector.append(range_translate(length_vector[j],almap))
		return translated_vector

def range_query(y,range_tuple):
	if range_tuple[0]<=y and y<range_tuple[1]:
		return True
	else:
		return False
