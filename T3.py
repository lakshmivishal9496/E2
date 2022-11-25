'''
first_number = 5
second_number = 3
third_number = 4.7
radius = 8.345
PI = 3.14
Next, calculate the circumference using the radius and PI variables,
store the result in a new variable. When all that is done it is time to
print it all to the screen in the following format:

5       +        3      =        8
5       +        4.7    =        9.7
The circumference is approximately 52.4
Use the \t and f-strings described in the course
literature to accomplish the format above.
'''
first_number = 5
second_number = 3
third_number = 4.7
radius = 8.345
PI = 3.14

print('\t first_number + second number is', first_number + second_number)

print('\t first_number + second number is', first_number + third_number)
circumference = 2 * (PI * radius)
print('f{circumference:.1f}')
