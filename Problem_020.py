# Solution to Project Euler - Problem 20
# Factorial Digit Sum by MaxxHolmes

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
#______________________________________________________________________________

import time
from math import factorial

start = time.time()

def solution():
	answer = sum(int(digit) for digit in str(factorial(100)))
	return answer

print(solution())
print(time.time() - start)