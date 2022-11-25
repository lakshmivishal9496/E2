'''
*
**
***
****
*****
******
'''
# for row in range(1, 7):
#     for col in range(row):
#         print('*', end='')
#     print()
'''
*****
*****
*****
*****
'''
# for row in range(4):
#     for column in range(5):
#         print('*', end='')
#     print()
'''
**********
********
******
****
**
'''
# for row in range(6, 0, -1):
#     for col in range(row):
#         print('*' * 2, end='')
#     print()
'''
* * * * *
 * * * *
* * * * *
 * * * *
'''
# for row in range(4):
#     if row % 2 == 0:
#         for col in range(10):
#             if col % 2 != 0:
#                 print(' ', end='')
#             elif col % 2 == 0:
#                 print('*', end='')
#     else:
#         for col in range(8):
#             if col % 2 != 0:
#                 print('*', end='')
#             elif col % 2 == 0:
#                 print(' ', end='')
#     print()

print('\n -- -- Fourth pattern -- -- \n')
current_char = '*'
for y in range(0, 4):
    for x in range(0, 9):
        print(current_char, end='')
        if current_char == '*':
            current_char = ' '
        else:
            current_char = '*'
    print()
