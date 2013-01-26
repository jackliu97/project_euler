def is_perfect_square(num):
	return ((num**0.5)%1==0)
for a in range(1, 1001):
	for b in range(1, 1001):
		c_sq = (a**2 + b**2)
		if(is_perfect_square(c_sq)):
			c = int(c_sq**0.5)
			if((a + b + c) == 1000):
				print(a * b * c)
				exit()