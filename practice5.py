# list1 = [1, 3, 5, 6]
# total = 0
# for i in list1:
#     total += i
# print(total)
# total = 0
# list2 = [x+x for x in list1]
# print(list2)
# values = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
# for row in values:
#     for col in row:
#         print(row, col)
country = ['', '', '']
keep_going = True
while keep_going:
    choice = int(input('which country you want to change: '))
    if 1 <= choice <= 3:
        country[choice - 1] = input('Enter the country name: ')
    elif choice == 9:
        keep_going = False
print(country)
