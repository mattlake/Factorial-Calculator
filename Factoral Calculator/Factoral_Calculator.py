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

play = input('Would you like to find the factoral number? y/n:  ')
while play=='y':
	start = int(input('Starting number to factor: '))
	print(factoral(start))
	play = input('Would you like to find another factoral number? y/n:  ')
if play=='n':
	print('Thanks for playing')