def div(num):
	print(num)
	for i in range(1, 20):
		if(num%i != 0):
			return False
	return True

num = 2520
while (div(num) != True):
	num += 2520

print(num)

