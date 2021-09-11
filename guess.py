import random
start = input('Input Min.Number: ')
end = input('Input Max.Number: ')
start = int(start)
end = int(end)

time = 0
time = int(time)

r = random.randint(start, end)

while True:
	time+= 1 
	guess = input('Guess a number:')
	guess = int(guess)
	if guess == r:
		print('Good job!')
		print('You made', time, 'guess in total!')
		break
	elif guess > r:
	    print('Wrong Andwer! Try it again')
	    print('Hint: Down!')
	elif guess < r:
	    print('Wrong Andwer! Try it again')
	    print('Hint: Up!')
	print('You have made', time, 'guess!')
 


