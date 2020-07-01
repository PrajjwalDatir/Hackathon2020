from sys import stdin
from decimal import *
count = int(stdin.readline())



for _ in range(count):
	pri = 0
	N = int(stdin.readline())
	x, y = map(int, stdin.readline().split())
	getcontext().prec = N + len(str(x//y))

	# print(x,y)
	# print(type(N))
	num = Decimal(x) / Decimal(y)
	# print(num)
	# num = num - Decimal(x) // Decimal(y)
	# print(num)
	if num > 0:
		num = str(num)
		arr = num.split(".")
		# print(arr)
		# num = arr[1]
		RES = list(map(int,str(arr[1])))
		# print(RES)
		for i in range(N):
			pri += RES[i]
		print(pri)
	else:
		print("0")