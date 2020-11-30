import sys


def UniqueDig(n): 
	count = 0
	digits = []
	while n != 0:
		curr = n%10
		digits.append(curr)
		n = n//10
		for i in range(len(digits)):
			if curr==i:
				return False
	return True
def countDigit(n): 
    if n == 0: 
        return 0
    return 1 + countDigit(n // 10) 

def factorial(n): 
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)  

test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	LR = list(sys.stdin.readline().split())
	L = int(LR[0])
	R = int(LR[1])
	# print("L is ", L)
	# print("R is ", R)
	Start = countDigit(L)
	End = countDigit(R)
	# print("Start is ", Start)
	# print("End is ", End)
	cnt = 0
	# print(UniqueDig(321))
	for num in range(L, R):
		# cnt += factorial(i)
		#start with 1...start such that it is > L
		
		if len(str(num)) == len(set(str(num))):

		for i in range(1,num):
			pass
		# if UniqueDig(my_num):
		# 	cnt += 1
	
	print(cnt)
		
