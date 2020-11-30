import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	AP = list(sys.stdin.readline().split())
	A = int(AP[0])
	B = int(AP[1])
	C = int(AP[2])
	D = int(AP[3])
	a = int(AP[4])
	b = int(AP[5])
	c = int(AP[6])
	d = int(AP[7])
	ava = [A,B,C,D]
	req = [a,b,c,d]
	how1 = A // a
	how2 = B // b
	how3 = C // c
	how4 = D // d
	k = [how1, how2, how3, how4]
	mx = max(how1, how2, how3, how4)
	for i in range(len(k)):
		if k[i] == mx:
			if ava[i] % req[i]:
				# print("k[i]:", k[i])
				mx += 1

	a1 = (mx - how1)*a - A % a
	b1 =  (mx - how2)*b - B % b
	c1 = (mx - how3)*c - C % c
	d1 = (mx - how4)*d - D % d
	# print(int(a1), int(b1), int(c1), int(d1))
	sys.stdout.write(str(a1) +" "+ str(b1)+" " + str(c1)+" " + str(d1)+ "\n")