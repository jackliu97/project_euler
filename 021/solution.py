def d(n):
	divs = [1]
	for i in range(2, int(n**0.5) + 1):
		if(n%i == 0):
			divs.append(i)
			divs.append(int(n/i))
	return sum(set(divs))

a_num = []

def test(a):
	global a_num
	b = d(a)
	if(d(b) == a and b != a):
		if a not in a_num and b not in a_num:
			a_num.append(a)
			a_num.append(b)
			
for i in range(2, 10001):
	test(i)

print(sum(a_num))

