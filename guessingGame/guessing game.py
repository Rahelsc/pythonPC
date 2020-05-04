import random

number = random.randint(0, 1000)
print(number)
while True:
    guess = int(input("please guess a number between 0 and 1000, if you wish to quit press -1"))
    if guess == -1:
        break
    print(guess)
    if guess < number:
        print("higher")
    elif guess > number:
        print("lower")
    else:
        print("you guessed it!!!")
        break