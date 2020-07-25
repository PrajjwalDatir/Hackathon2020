# Nagini_Magic_Spell.py
from sys import stdin

n, k, a= map(str , stdin.readline().split(" "))
n = int(n)
k = int(k)

a = list(a)
# print(a)

# print(n,k,string)


maximum = 0
#a = 11100000 	k = 3

for index in range(n): #0 1 2 3 4 5
	# print("Enter NEW LOOP------")
	count = 0
	chance = k
	flag = 0

	i = index
	while i < n: # n = 6 , a = 010011 if k = 2
		# print(a[i])
		# print(i)
		# print(f"Maximum is {maximum}")
		if flag:
			# print("break")
			break
		if int(a[i]):
			# print("spotted 1")
			count += 1
		elif chance:
			# print("spotted chance")
			count = count + chance
			if count > maximum:
				maximum = count

			i = i + chance - 1
			chance = 0
		else:
			# print("spotted void")
			flag = 1
		i += 1
	if count > maximum:
		maximum = count
				
print(maximum)