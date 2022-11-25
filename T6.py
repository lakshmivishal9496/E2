'''
You and your best friend was discussing how much money you
would end up with if you put
away 20 000kr on a bank account and did not touch it for 20 years.
After the discussion ended
you decided to write a script that
calculated how much money one would end up with given that the interest is 5%.
Use the following formula to calculate the compound interest:
FV = PV * (1 + r)**n
FV = Future value
PV = Present value (Starting value)
r = The interest as a decimal value
n = number of years
A more in-depth description, with examples, of compound interest can be
found here (Links to an external site.). Basically the same task is also
listed under Programming Exercises in the end of Chapter 2 in
the course literature. There are many more tasks listed,
have a look if you want more practice.
'''
pv = int(input('Enter the present value'))
r = float(input('Enter the rate of interest'))
n = int(input('Enter the number of years'))
fv = pv * (1+r)**n
print(f'After {n} year you will have {fv:.2f}')
