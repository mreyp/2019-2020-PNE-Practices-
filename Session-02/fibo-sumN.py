# Session 2-Exercise 3

def fibosum(n):
    a = 0
    m = 1
    res = 1
    sum = 0

    for i in range(0, n - 1):
        sum = a + m
        a = m
        m = sum
        res +=sum

    return res


print('Sum of the first 5 terms of the Fibonacci series:', fibosum(5))
print('Sum of the first 10 terms of the Fibonacci series:', fibosum(10))
