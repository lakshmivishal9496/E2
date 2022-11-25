print('    * |  1   2   3   4   5   6   7   8   9   10')
print('     ------------------------------------------')
for r in range(1, 11):
    print(f'{r:4}  |', end='')
    for c in range(1, 11):

        res = r * c
        print(f'{res:4}', end='')
    print()
    
    

