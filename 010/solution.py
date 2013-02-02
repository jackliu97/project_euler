def prime(num):
	top = int(num**0.5) + 1
	for i in range(1, top):
		if((num%i == 0) and (i > 1)):
			return False
	return True

primes = []
checks = [2]

#primes can only be odd number after 2.
for i in range(3, 2000000):
	if(i%2==1):
		checks.append(i)

for i in checks:
	if(prime(i)):
		primes.append(i)

print(sum(primes))
