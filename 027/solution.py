def prime(num):
	top = int(num**0.5) + 1
	for i in range(1, top):
		if((num%i == 0) and (i > 1)):
			return False
	return True

def p_fun(a, b):
	n = 0
	while prime(abs(n**2 + a*n + b)):
		n += 1
	return abs(n)

largest = 0
largest_a = 0
largest_b = 0
for a in range(-1001, 1001):
	for b in range(-1001, 1001):
		x = p_fun(a, b)
		if x > largest :
			largest = x
			largest_a = a
			largest_b = b

print(largest_a*largest_b)