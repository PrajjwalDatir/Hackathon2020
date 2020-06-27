#test.py
import sys
i = 1
S = list(input())
S = list(map(lambda x:x, S))
# print(S)
# for line in sys.stdin.readline() :
# 	S.append(line.split())
# 	i = i + 1
# S = list(sys.stdin.read().split())
K = int(sys.stdin.readline())

#AAB BCD ABC


# print(S)
# print(K)
for i in range(len(S) // K):
	u = S[i*K : (i+1)*K]
	# print(u)
	for j in range(K): #012
		cnt = 0
		for m in range(j): #0,01
			if u[j] == u[m]:
				cnt = 1
		if cnt == 0:
			print(*u[j], end="")
	print()