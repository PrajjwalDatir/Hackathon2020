import sys
	
AP = list(sys.stdin.readline().split())
start = int(AP[0])
end = int(AP[1])

prime = []
for val in range(start, end + 1): 
	if val > 1:
		if val == 2:
			prime.append(val)
		for n in range(2, val//2 + 2):
			if (val % n) == 0:
				break
			else:
				if n == val//2 + 1:
					prime.append(val)
add = [prime[0]]
#print(len(prime))
for i in range(1, len(prime)):
	add.append( prime[i] + add[i-1] )

# print(prime)
# print(add)

cnt = 0
for val in add:
	val = int(val)
	if val > 1:
		if val == 2:
			cnt += 1
		for n in range(2, val//2 + 2):
			if (val%n) == 0:
				break
			else:
				if n == (val//2 + 1):
					cnt += 1


print(cnt)
