#generate number with no repeated
# where all the digits 1-9 (excluding 0) appear at most once but one condition is that 
# the number should contain all the digits less than the largest digit in the number (but not zero).
"""generate number betn two digits
let say 3200 and 10000
3xxx 3xxx
32xx 32xx
320x

we have digits = []
"""
start = 3200 
end = 100000
mindigit = 4
maxdigit = 6
digits = []
for i in range(1, 4+1):
	digits.append(i)
print(digits)
num = start // pow(10, mindigit - 1)
print(num)
for i in range(1,4):
	