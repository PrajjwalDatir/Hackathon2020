import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	NM = list(sys.stdin.readline().split())
	N_bag = int(NM[0])
	M_eat = int(NM[1])
	E_bag = list(sys.stdin.readline().split())
	# here E[0] energy of first bag etc
	for i in range(len(E_bag)):
		E_bag[i] = int(E_bag[i])

	if not M_eat % N_bag:
		print("0")
	else:
		# min(E_bag)
		for i in range(M_eat):
			if not M_eat % N_bag - i:
				print(min(E_bag)*(len(E_bag) - 1))