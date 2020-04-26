a = 0
FIRST_NUMBER = 3
SECOND_NUMBER = 5

for x in range(1, 1000):
    if x % FIRST_NUMBER == 0 or x % SECOND_NUMBER == 0:
        a += x


print(a)

