# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the math module, which contains features for working with mathematics
import math

# TODO: the math module contains lots of pre-built functions
print("The square root of 16 is", math.sqrt(16))

# TODO: in addition to functions, some modules contain useful constants 
print("Pi is", math.pi)

# TODO: try some of the math functions for yourself here:
#* Factorial
print("The factorial of 5 is", math.factorial(5))
#* Least common divisor
print("The greatest common divisor of 24 and 256 is", math.gcd(24, 256))
#* Lcm = the smallest number that two or more numbers can divide into evenly.
print("The least common multiple of 4 and 5 is", math.lcm(4, 5))
#* Permutation = Return the number of ways to choose k items from n items without repetition and with order
print("How many ways can 3 pool balls be arranged out of 16 balls? A:", math.perm(16, 3))
print("How many ways can the 16 balls be arranged? A:", math.perm(16))
#* Combination = Return the number of ways to choose k items from n items without repetition and without order
print("How many combinations of 3 pool balls out of 16 are there? (order doesn't matter) A:", math.comb(16,3))
print("How many combinations of 16 pool balls are there? A:", math.comb(16, 16))
