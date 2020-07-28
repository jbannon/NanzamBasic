import numpy as np



def make_bins(vectors, w):
	pass

def make_random_directions(num_vectors, dimension, p=2):
	if p==1:
		return np.random.standard_cauchy((num_vectors,dimension))
	elif p==2:
		return np.random.standard_normal((num_vectors,dimension))
	else:
		print("invalid p")



print(make_random_directions(10,3,1))