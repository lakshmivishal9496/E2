# for count in range(10, 0, -2):
#     print('*' * count)
# for count in range(0, 10, 2):
#     print('*' * count)
'''
* * * * *
 * * * *
* * * * *
 * * * *
'''
for i in range(5):
    if i % 2 != 0:
        for j in range(9):
            if j % 2 == 0:
                print(' ', end='')
            else:
                print('*', end='')
    else:
        for j in range(9):
            if j % 2 == 0:
                print('*', end='')
            else:
                print(' ', end='')
    print()
    
