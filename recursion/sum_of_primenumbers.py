"""
question 2

sum of numbers in a series
"""


def sum_numbers(n: int):
    if n < 2:
        return 1
    return sum_numbers(n - 1) + n


print(sum_numbers(5))
