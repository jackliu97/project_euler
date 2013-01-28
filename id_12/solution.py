def tri(num):
	return int(num * (num+1)/2)


def factors(num):
	div = 0
	for i in range(1, int(num**0.5) + 1):
		if(num%i == 0):
			div += 1
	return div * 2

i = 1
while(factors(tri(i)) <= 500):
	i += 1

print(tri(i))