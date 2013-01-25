def fib(largest_number):
	result = [];
	i=1
	result.append(i)
	i+=i
	result.append(i)

	while i < largest_number:
		i = result[-1] + result[-2]
		result.append(i)

	return result


fib_result = fib(4000000)

ans = 0

for i in fib_result:
	if(i%2 == 0):
		ans += i

print(ans)
