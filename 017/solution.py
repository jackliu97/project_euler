def ones(num):
	if(num == 0):
		return ''
	if(num == 1):
		return 'one'
	elif (num == 2):
		return 'two'
	elif (num == 3):
		return 'three'
	elif (num == 4):
		return 'four'
	elif (num == 5):
		return 'five'
	elif (num == 6):
		return 'six'
	elif (num == 7):
		return 'seven'
	elif (num == 8):
		return 'eight'
	elif (num == 9):
		return 'nine'
	elif (num == 10):
		return 'ten'

def teens(num):
	if(num == 11):
		return 'eleven'
	elif (num == 12):
		return 'twelve'
	elif (num == 13):
		return 'thirteen'
	elif (num == 14):
		return 'fourteen'
	elif (num == 15):
		return 'fifteen'
	elif (num == 16):
		return 'sixteen'
	elif (num == 17):
		return 'seventeen'
	elif (num == 18):
		return 'eighteen'
	elif (num == 19):
		return 'nineteen'
	elif (num == 20):
		return 'twenty'

def tens(num):
	if(num <= 10):
		return ones(num)
	elif(num <= 20):
		return teens(num)
	elif(num < 30):
		return 'twenty%s'%ones(num-20)
	elif(num < 40):
		return 'thirty%s'%ones(num-30)
	elif(num < 50):
		return 'forty%s'%ones(num-40)
	elif(num < 60):
		return 'fifty%s'%ones(num-50)
	elif(num < 70):
		return 'sixty%s'%ones(num-60)
	elif(num < 80):
		return 'seventy%s'%ones(num-70)
	elif(num < 90):
		return 'eighty%s'%ones(num-80)
	elif(num < 100):
		return 'ninety%s'%ones(num-90)
	elif(num == 100):
		return 'onehundred'

def hundreds(num):
	if(num < 100):
		return tens(num)
	elif(num < 1000):
		str_num = str(num)
		str_and = 'and'
		if(int(str_num[1:3]) == 0):
			str_and = ''
		return '%shundred%s%s'% (ones(int(str_num[0])), str_and, tens(int(str_num[1:3])))
	else:
		return 'onethousand'


def read_logic(num):
	if(num <= 10):
		return ones(num)
	elif(num <= 20):
		return teens(num)
	elif(num <= 100):
		return tens(num)
	elif(num <= 1000):
		return hundreds(num)
l = 0
for i in range(1, 1001):
	l += len(read_logic(i))
print(l)