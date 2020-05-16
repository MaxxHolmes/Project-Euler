# Solution to Project Euler - Problem 18
# Maximum Path Sum I by MaxxHolmes

# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23.

# Find the maximum total from top to bottom of the triangle given (15 rows)
#______________________________________________________________________________

import time
start = time.time()

# If we arrange the triangle as a matrix then we can approach this
# as a maximum sum cost problem.
# We can start at the bottom of the matrix and determine which of the numbers
# avaliable leads to the highest sum, and add it.
# The top of the triangle then becomes the largest possible path sum.

def maximum_path_sum(triangle, rows):

	for j in range(rows-2, -1, -1):
		for i in range(j+1):

			if (triangle[j+1][i] > triangle[j+1][i+1]):
				triangle[j][i] += triangle[j+1][i]
			else:
				triangle[j][i] += triangle[j+1][i+1]

	return triangle[0][0]

triangle = [
[75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[95, 64,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[17, 47, 82,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[18, 35, 87, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[20,  4, 82, 47, 65,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[19,  1, 23, 75,  3, 34,  0,  0,  0,  0,  0,  0,  0,  0,  0],
[88,  2, 77, 73,  7, 63, 67,  0,  0,  0,  0,  0,  0,  0,  0],
[99, 65,  4, 28,  6, 16, 70, 92,  0,  0,  0,  0,  0,  0,  0],
[41, 41, 26, 56, 83, 40, 80, 70, 33,  0,  0,  0,  0,  0,  0],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29,  0,  0,  0,  0,  0],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,  0,  0,  0,  0],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,  0,  0,  0],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,  0,  0],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,  0],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

print(maximum_path_sum(triangle, 15))
print(time.time() - start)