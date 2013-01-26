from math import *

def prime(num):
	top = int(sqrt(num)) + 1
	for i in range(1, top):
		if((num%i == 0) and (i > 1)):
			return False
	return True


count = 0
for i in range(2, 10001**2):
	if(prime(i)):
		print(i)
		count += 1

		if(count == 10001):
			print(i)
			exit()