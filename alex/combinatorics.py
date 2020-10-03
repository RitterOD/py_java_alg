
def generate_permutation_imp(cur_perm, cur_ind, marks):
	#print("cur_perm = ", cur_perm, " cur_ind = ", cur_ind, " marks = ", marks)
	if cur_ind == len(marks):
		print(cur_perm)
	else:
		clean_marks = list(marks)
		for i in range(len(marks)):
			if not marks[i]:
				new_marks = list(clean_marks)
				new_marks[i] = True
				marks[i] = True
				new_perm = list(cur_perm)
				new_perm.append(i)
				generate_permutation_imp(new_perm, cur_ind + 1, new_marks)



def generate_permutation(n):
	marks = [False] * n
	generate_permutation_imp([], 0, marks)
	return None


if __name__ == '__main__':
	print('combinatorics algorithm example')
	rv = generate_permutation(4)
	#for e in rv:
	#	print(e)