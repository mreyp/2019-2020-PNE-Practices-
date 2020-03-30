# --1 + 2 + 3 .... + 20
# --1 +...100


def sumN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


print('The sum of the 20 first integers: ', sumN(20))
print('The sum of the 100 first integers: ', sumN(100))
