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
	
	count = 0
	chance = k
	flag = 0
	for i in range(index, n): # n = 6 , a = 010011 if k = 2
		# print(a[i])
		if flag:
			# print("break")
			break
		if int(a[i]):
			# print("spotted 1")
			count += 1
		else:
			if chance:
				# print("spotted 0 but have magic")
				count += 1
				chance -= 1
			else:
				# print("spotted 0 but not magic")
				if count > maximum:
					# print(f"maximum updated {maximum}")
					maximum = count
				count = 0
				chance = k
				flag = 1
	if count > maximum:
		maximum = count
				
print(maximum)


