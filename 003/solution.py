from math import *

def prime(num):
	top = int(sqrt(num)) + 1
	for i in range(1, top):
		if((num%i == 0) and (i > 1)):
			return False
	return True


num = 600851475143
factor_list = []
for i in range(2, ceil(sqrt(num))):

	if(num%i == 0): #check for factor
		if(prime(i)): #check for prime
			factor_list.append(i)
			
print(factor_list[-1])

