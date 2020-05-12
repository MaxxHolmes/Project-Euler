# Solution to Project Euler - Problem 2
# MaxxHolmes

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#___________________________________________________________________________

# As any 6 digit palindrome we create must follow the formula:
# 100000a + 10000b + 1000c + 100c + 10b + 1a = 100001a + 10010b + 1100c = xy
# therefore
# 11(9091a + 910b + 100c) = xy

def palindrome_checker(n):
	if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3]:
		return True
	else:
		return False

# We can start the search from 999 and 990, as one must be a multiple of 11,
# and 990 is the largest 3 digit multiple of 11.
answer = 0
for x in range(999, 100, -1):
	for y in range(990, 100, -11):
		n = x*y
		if n > answer and palindrome_checker(str(n)):
			answer = n
		else:
			pass

print(answer)
