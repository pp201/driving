country = input('What is your nationality: ')
age = input('Enter your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('Bro, go get the license. ')
	else:
		print('Sorry, you are too young for the drive license. ')
elif country == 'USA':
	if age >= 16:
		print('Bro, go get the license. ')
	else:
		print('Sorry, you are too young for the drive license. ')
else:
	print('Sorry man')