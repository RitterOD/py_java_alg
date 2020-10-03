import random

def rnd_lst_gen(low, hi, len):
	rv = []
	for i in range(len):
		rv.append(random.randint(low, hi))
	return rv
	
if  __name__ == "__main__":
	rnd_lst = rnd_lst_gen(0, 50, 15)
	print("RANDOM LIST\n")
	print(*rnd_lst)