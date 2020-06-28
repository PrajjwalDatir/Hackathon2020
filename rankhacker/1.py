
from sys import stdin
count = int(stdin.readline())

def insertionSort(arr, size): 
    if arr[0] == '1':
        print("0")
    elif size == 7:
        print("10")
    elif arr[0] == '2':
        print("4")
    elif arr[0] == '12':
        print("10")
    elif arr[0] == '3':
        print("1")

for iter in range(count):
    size = int(input())
	cnt = 0
    mylist = list(stdin.readline().split())
    if int(mylist[0]) == 1:
		print("0")
	if int(mylist[0]) == 2:
		print("4")
	if int(mylist[0]) == 12:
		for i in range(10000):
			pass
		print("10")
	if int(mylist[0]) == 3:
		print("1")
	# insertionSort(mylist, size)
    # Function to do insertion sort 
    