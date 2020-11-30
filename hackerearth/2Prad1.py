import sys


def sum_of_digits(Y):
	sum = 0
	while Y:
		sum += Y%10
		Y = Y//10
	return sum

test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	
	AP = list(sys.stdin.readline().split())
	a = int(AP[0])
	d = int(AP[1])
	L = int(AP[2])
	R = int(AP[3])
	# Y is a+id
	Y = a
	ans = 0
	for i in range(L, R+1):
		Y = a + (i-1)*d
		while Y >= 10:
			Y = sum_of_digits(Y)
			# print(Y)
			# ans = ans + Y
		# print(Y) 
		ans += Y
	print(ans)