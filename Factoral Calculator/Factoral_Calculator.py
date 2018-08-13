#Simple program loop to find the factorial of any given number

def factoral(n):
	result = 0
	while n>=0:
		if(n<=0):
			return result
		else:
			if(result==0):
				result = n
				n-=1
			else:
				result *= n
				n-=1

play = input('Would you like to find the factorial number? y/n:  ')
while play=='y':
	start = int(input('Starting number to factor: '))
	print(factoral(start))
	play = input('Would you like to find another factorial number? y/n:  ')
if play=='n':
	print('Thanks for playing')