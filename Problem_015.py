# Solution to Project Euler - Problem 15
# Lattice Paths by MaxxHolmes

# Starting in the top left corner of a 2×2 grid, and only being able to move 
# to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?
#______________________________________________________________________________

import time
from math import factorial

start = time.time()

# Starting at (0, 0), and wanting to get to (20, 20) - 40 moves are needed.
# At (0, 0) there are 40 possible moves you could make (i.e. go to any of 40 squares)
# for a unique path. Once you take a move (x, y) there are then 40 - x - y steps.
# Therefore, we know that 40! is the upper limit.

# There is however, boundaries which when hit, produce only once unique path
# from that point onwards. There are 20 - x and 20 - y ways to hit these boundary
# points from each co-ordinate (20!) and (20!), for (20!)(20!) from (0, 0). 
# Therefore, the total number of paths is: (x + y)! / x! * y!

x = 20
y = 20
print(factorial(x+y) // (factorial(x) * factorial(y)))
print(time.time() - start)
