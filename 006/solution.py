import math

square_sum = 0 #square first, sum second
sum_square = 0 #sum first, square second

for i in range(1, 101):
	sum_square += i
sum_square = pow(sum_square, 2)

for i in range(1, 101):
	square_sum += pow(i, 2)

print(sum_square - square_sum)