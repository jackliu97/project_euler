#f = first
#i = max iter
def pattern(f, inc, i):
	c = 0
	x = []
	m = []

	m.append(f)
	while m[-1] < i:

		x.append(inc)
		y = f + sum(x)

		if int(y) > int(i):
			break
		m.append(y)
		inc = inc + 8
		c += 1

	return m
	
max_loop = 1001**2
print(sum(pattern(3, 10, max_loop)) + sum(pattern(5, 12,max_loop)) + sum(pattern(7, 14, max_loop)) + sum(pattern(9, 16, max_loop)) + 1)

