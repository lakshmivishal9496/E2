def fibo(n):
    first = 0
    second = 1
    if n <= 1:
        print(first)
    elif n >= 2:
        print(first)
        print(second)
        for i in range(2, n):
            sum = first + second
            first = second
            second = sum
            print(sum)


fibo(5)
