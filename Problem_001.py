# Solution to Project Euler - Problem 1
# MaxxHolmes

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# ________________________________________________________________________________________________

# There are two things to consider when solving this problem:
#	-	How do we get the multiples of 3 and 5 all the way to 999
#	-	How do we exclude numbers that are multiples of both 3 and 5 (multiples of 15)

# This is a fairly straight forward problem to solve, by choosing the condition x % 3 == 0,
# OR x % 5 == 0, then multiples of 15 are not counted twice. By additing this condition to
# x for x in range(1000), we return a list of multiples of 3 or 5 from 0 to 999. Then all
# we need to do is sum them for the solution!


def solution():

	answer = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))

	return str(answer)

print(solution())