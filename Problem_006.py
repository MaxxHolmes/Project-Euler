# Solution to Project Euler - Problem 6
# Sum Square Difference by MaxxHolmes

# The sum of the squares of the first 10 natural numbers is
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first 10 natural numbers is
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# The difference is 3025-385

# Find the difference between the sum of the squares of the first 100 numbers and the
# square of the sum
#_____________________________________________________________________________________________

import time
start = time.time()

def solution():

	n = 100
	x = sum(i for i in range(1, n+1))
	y = sum(i**2 for i in range(1, n+1))
	return str(x**2 - y)

print(solution())
print(time.time() - start)