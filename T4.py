'''
Your employer has asked you to create a script that reads
some information about a person and then outputs the read information
to the screen in a nice, very specific format.  The information
that shall be read is:
The persons first name
The persons last name
How old the person is
The persons phone number
An example of the output format can be seen below:

Anna Person was born in 1995 and can be contacted at 0709-123456.
Note that the year the person was born must be calculated using entered age.
'''

first_name = input('Enter the first name')
last_name = input('Enter the last name')
age = int(input('How old are you'))
phone_number = int(input('Enter your phone number'))

persons_age = 2022 - age

print(f'{first_name} {last_name} was born in ')
print(f'{persons_age} and can be contacted at {phone_number}')
