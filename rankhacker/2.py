from sys import stdin
N = int(stdin.readline())
for _ in range(N):
	mylist = list(stdin.readline().split())
	# odd pos words
	# even pos numbers
	# print(mylist)
	# print(len(mylist))
	newlist = []
	numlist = []
	for i in range(len(mylist)):
		if not i%2:
			newlist.append(mylist[i].lower())
		else:
			numlist.append(int(mylist[i]))
	newlist.sort()
	numlist.sort()
	j = 0
	k = 0
	for i in range(len(mylist)):
		if not i%2:
			print(newlist[j].lower(), end=" ")
			j += 1
		else:
			print(numlist[k], end=" ")
			k += 1
	# print(newlist)
	# print(numlist)
	print()