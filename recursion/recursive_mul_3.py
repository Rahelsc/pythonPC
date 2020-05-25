# exercise 1 - implementing f(n) = 3 * n


def mul_3_of_3(n: int):
    if n < 1:
        return 0
    else:
        return mul_3_of_3(n - 1) + 3


print(mul_3_of_3(2))
