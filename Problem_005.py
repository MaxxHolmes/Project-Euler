# Solution to Project Euler - Problem 5
# Smallest multiple by MaxxHolmes

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisble by all the numbers from 1 to 20?
#_____________________________________________________________________________________________

def divider(n):

	for i in range(2, 21):
		if (n % i) != 0:
			return False
	return True

n = 20
while True:
	if divider(n):
		break
	else:
		n = n + 20

print(n)
