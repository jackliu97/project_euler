from itertools import *

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



#
# Not used: Much Much faster approach.
# Find combinations of prime factors to get number of factors.
#
def p_factors(num):
	s = []
	for i in range(2, num+1):
		if(num%i == 0):
			s.append(i)
			x = num/i
			return (s + p_factors(int(x)))
	return s

def prime_combination_products(primes, r):
	ans = []
	for c in combinations(primes, r):
		ans.append(c)
	return list(set(ans))


def factors_quick(num):
	primes = p_factors(num)
	products = [1]
	for l in range(1, len(primes)+1):
		products += prime_combination_products(primes, l)

	return len(products)

