
def get_months(year):
	if(year%4 == 0 and year%100 != 0) or (year%400 == 0): #leap year.
		return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	else:
		return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

inc = 0 #number of days passed.
sun = 0 #number of sundays.
for y in range(1900, 2001):
	months = get_months(y)
	m_name = 0
	for m in months:
		m_name += 1
		for d in range(1, m+1):
			inc += 1
			if(inc%7 == 0 and d == 1 and y >= 1901 and y <= 2000):
				sun += 1
print(sun)
