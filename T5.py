'''
Task 5
A friend of yours is about to embark on a road trip and needs an easy way
to get an approximation of how long it will take him to reach a destination.
He knows you have started to learn programming and have
asked for your assistance.
Create a script where the user inputs the total distance to drive
and an estimated average speed.
Using this information, the script shall calculate an estimate of how long it
will take to drive
the specified distance using the specified average speed.
The result shall be printed to the screen when the calculation is done.
'''

distance = int(input('Enter the distance'))
speed = int(input('Enter the speed'))

time = distance / speed
print(f'The time taken to travel is: {time} hours')
