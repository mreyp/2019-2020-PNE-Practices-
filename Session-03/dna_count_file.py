counter = 0
a = 0
g = 0
c = 0
t = 0


with open('dna', 'r') as f:
    for line in f:
        for letter in line:
            counter += 1
            if letter == 'A':
                a += 1
            elif letter == 'G':
                g += 1
            elif letter == 'C':
                c += 1
            elif letter == 'T':
                t += 1

print('Total length:', counter)
print('A:', a)
print('G:', g)
print('C:', c)
print('T:', t)
