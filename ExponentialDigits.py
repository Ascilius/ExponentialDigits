from math import *

debug = False

def expDig(n):
	# getting digits
	digits = []
	temp = n
	while True:
		digit = temp % 10
		digits.append(digit)
		temp = int(temp / 10)
		if temp == 0:
			break
	if debug:
		print(digits)

	# calculating
	total = digits[0]
	for i in range(1, len(digits)):
		try:
			total = pow(digits[i], total)
		except OverflowError:
			total = float('inf')
			break
	total = sqrt(total)
	if debug:
		print(total)

	# checking
	# print(n, ("==" if total == n else "!="), total)
	return total == n

"""
# wrong method (parentheses)
def expDig(n):
	# getting digits
	digits = []
	temp = n
	while temp > 0:
		digit = temp % 10
		digits.insert(0, digit)
		temp = int(temp / 10)
	if debug:
		print(digits)

	# calculating
	total = digits[0]
	for i in range(1, len(digits)):
		try:
			total = pow(total, digits[i])
		except OverflowError:
			total = float('inf')
			break;
		if debug:
			print(total)
	total = sqrt(total)
	if debug:
		print(total)

	# checking
	print(n, ("==" if total == n else "!="), total)
"""

if __name__ == "__main__":
	n = 0
	while True:
		if expDig(n):
			print(n)
		n += 1 # next number
	
	# expDig(262144)