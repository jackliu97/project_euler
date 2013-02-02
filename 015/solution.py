from math import *

# (2n)!/n!^2
def number_of_paths(size):
	return int(factorial(2*size)/(factorial(size)**2))

print(number_of_paths(20))