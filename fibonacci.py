def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        a = b
        b = a + b