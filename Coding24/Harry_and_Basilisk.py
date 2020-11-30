#Harry_and_Basilisk.py
from sys import stdin

n, x, y= map(int , stdin.readline().split(" "))

# print(f"n is {n} , x is {x}, y is {y}")

Basilisk = list(map(int, stdin.readline().split()))
Basilisk = sorted(Basilisk)
# print(Basilisk)
mana = Basilisk[0] * y
# mana = 0
soldier = Basilisk[0]
for i in range(n):
	# print(f"Basilisk: {Basilisk[i]}")
	# print(f"Soldier: {soldier}")
	if soldier >= Basilisk[i]:
		# print(f"Soldier winning with army of: {soldier}")
		soldier += Basilisk[i]
	else:
		mana_increase = Basilisk[i] - soldier
		mana += ((mana_increase) * y)
		# print(f"increasing mana to: {mana}")
		soldier += mana_increase
		soldier += Basilisk[i]
# print(f"mana is: {mana}")
print(mana + ((n-1) * x))