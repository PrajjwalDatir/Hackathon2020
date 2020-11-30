def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

from sys import stdin
N = int(stdin.readline())
summ = 2
cnt = 0
flag = 0
if N == 2:
	print("0")
	flag = 1
for i in range(3, N):
	if flag:
		break
	if isPrime(i):
		summ += i
		if summ >= N:
			flag = 1
		elif isPrime(summ):
			cnt += 1
print(cnt)