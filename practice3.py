# user_input = int(input('Enter number in range 2 to 99: '))
# isPrime = True
# for i in range(2, user_input):
#     if user_input % i == 0 and i != user_input:
#         isPrime = False
# if isPrime:
#     print('Prime')
# else:
#     print('Not Prime')
def fibo(count):
    first = 0
    second = 1
    if count == 1:
        print(first)
    else:
        print(first)
        print(second)
        for i in range(2, count):
            sum = first + second
            first = second
            second = sum
            print(sum)


fibo(9) 