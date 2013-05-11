def pwr(n): return (n == sum([int(i)**5 for i in str(n)]))
print(sum([i for i in range(2, 236196) if pwr(i) == True]))