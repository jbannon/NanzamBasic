import numpy as np 
import sys





def generate_hash_func(w,k):
	if k>=w:
		print('error')
		sys.exit(0)
	indices = np.arange(1,w)
	func_dex = np.random.choice(indices,k,replace=True)
	func = lambda s: ''.join( [ s[i] for i in func_dex])
	return func


def make_hash_family(w,k,l):
	''' makes l hash functions'''
	funs = []
	for j in range(0,l):
		temp = generate_hash_func(w,k)
		funs.append(temp)
	return funs


def family_hash(hash_fam,s):
	return [hash_fam[i](s) for i in range(len(hash_fam))]

def main():
	z = np.random.choice(['A','T','C','G'],20,replace=True)
	test = generate_hash_func(len(z),3)
	print(test)
	print(test(z))
	hash_fam = make_hash_family(len(z),int(np.floor(len(z)/2)),20)
	tt = family_hash(hash_fam,z)
	print(tt)


if __name__ == '__main__':
	main()
