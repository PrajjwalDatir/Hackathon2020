N = int(input())

if N == 1:
	print("1")
elif N == 2:
	print("1 1\n1 1")
elif N % 2:
	for i in range(N):
		for j in range(N):
			if j == N - 1:
				if (i + j)%2:
					print("1", end="")
				else:
					print("0", end="")
			else:
				if (i+j)%2:
					print("1", end=" ")
				else:
					print("0", end=" ")
		print()
elif N % 2 == 0:
	for i in range(N):
		for j in range(N):
			if j == N - 1:
				print("0", end="")
			else:
				print("0", end=" ")
		print()