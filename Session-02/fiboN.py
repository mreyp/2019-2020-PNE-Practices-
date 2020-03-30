# Session 2--Exercise 2


def fibon(n):
    a = 0
    m = 1
    sum = 0
    for i in range(0, n - 1):
        sum = a + m
        a = m
        m = sum
    return sum


print('5th Fibonacci term:', fibon(5))
print('10th Fibonacci term:', fibon(10))
print('15th Fibonacci term:', fibon(15))
