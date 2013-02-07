def d(n):
	divs = [1]
	for i in range(2, int(n**0.5) + 1):
		if(n%i == 0):
			divs.append(i)
			divs.append(int(n/i))
	return sum(set(divs))


abundant = []
s = 0
for i in range(1, 28124):
	if(i < d(i)):
		abundant.append(i)
	if not any((i - j) in abundant for j in abundant): s += i

print(s)