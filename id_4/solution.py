from math import *

def is_palindromic(num):
	num_str = str(num)

	hlf = floor((len(num_str)/2))

	for i in range(0, hlf):
		if(num_str[i] != num_str[-(i+1)]):
			return False

	return True

#skip
# 1. all divisible by 10
# 2. all divisible by 5 (I'm pretty sure it won't end and start in 5)
is_pal = []
for x in range (101, 999):
	if(x%10 == 0):
		continue

	if(x%5 == 0):
		continue

	for y in range(101, 999):
		if(y%10 == 0):
			continue

		if(y%5 == 0):
			continue

		z = x*y
		if(is_palindromic(z)):
			is_pal.append(z)
is_pal.sort()
print(is_pal[-1])


