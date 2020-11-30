import sys
test_cases = int(sys.stdin.readline())
for i_iter in range(test_cases):
	AP = list(sys.stdin.readline().split())
	Health = int(AP[0])
	Armor = int(AP[1])
	cnt = 1
	while Health > 0 and Armor > 0:
		Health += 3
		Armor += 2
		if (Armor - 10) <= 0:
			if (Health - 20) > 0:
				Health -= 20
				Armor += 5
				cnt += 2
				# print("here1") 
			else:
				Health -= 5
				Armor -= 10
				# print("here2") 
		elif (Health - 5) <= 0:
			Health -= 5
			Armor -= 10
			# print("here3") 
		else:
			Health -= 5
			Armor -= 10
			cnt += 2
	print(cnt)
