# Solution to Project Euler - Problem 9
# Special Pythagorean Triplet by MaxxHolmes

#A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a^2 + b^2 = c^2

# There is exactly one pythagorean triplet for which a + b + c = 1000
# Find the product abc for that triplet.
#_____________________________________________________________________

import time
start = time.time()

def pythagorean_triplet_product(n):

	for a in range(1, n+1):
		for b in range(1, n+1):
			c = n - a - b
			if (a**2 + b**2 == c**2):
				print(a)
				print(b)
				print(c)
				return a*b*c

print(pythagorean_triplet_product(1000))
print(time.time() - start)
