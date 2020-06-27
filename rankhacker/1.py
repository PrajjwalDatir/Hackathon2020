# Python program to check if two strings are anagrams of 
# each other 
import sys


# Function to check whether two strings are anagram of 
# each other 
def areAnagram(str1, str2): 

	if len(str1) < len(str2):
		return 0

	for i in range(len(str1) - len(str2)): #0 1 2 3
		cnt = 0
		for j in range(len(str2)):# 0 1 2
			if str1[j + i] == str2[j]:
				cnt += 1
		if len(str2) == cnt:
			return 1

	return 0

# Driver program to test the above functions 


str1 = input()
repeat = int(input())

str2 = ""
pointer = 0
for i in range(repeat):
	AP = list(sys.stdin.readline().split())
	letter = str(AP[0])
	rot = int(AP[1])

	if letter == 'L':
		pointer += rot
		#L 2	
	elif letter == 'R':
		pointer -= rot

	str2 += str1[pointer]

# print(str2)
if areAnagram(str1, str2): 
	print("YES")
else: 
	print("NO")


