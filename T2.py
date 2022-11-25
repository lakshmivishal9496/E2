'''
The first goal of this task is to read the users name, and two numbers from
the keyboard
After having read the information the two numbers shall be
added together and the sum stored
in a new variable. Finally all the information, the name,
the two numbers and the sum shall be printed to the screen
'''
user_name = input('Enter your name')
first_number = int(input("Enter the first number"))
second_number = int(input("Enter the second number"))
total = first_number + second_number
print(f'The username is {user_name}')
print(f'The first number is {first_number}')
print(f'The second number is {second_number}')
print(f'The sum of both number is {total}')
