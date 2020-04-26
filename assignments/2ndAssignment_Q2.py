def odd_or_even(user_input):
    if user_input % 4 == 0:
        print("this number is divisible by 4")
    elif user_input % 2 == 0:
        print("Even")
    else:
        print("odd")


def is_divisible(divisible, divider):
    if divisible % divider == 0:
        print("is divisible")
    else:
        print(divisible, 'is not divisible by', divider)


input_from_user = int(input("please enter a number "))
odd_or_even(input_from_user)

input1 = int(input("please enter a number you want to divide "))
input2 = int(input("please enter a number you to divide by "))
is_divisible(input1, input2)


