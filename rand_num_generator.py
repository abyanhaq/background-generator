import sys
import random

num_1 = 1
num_2 = 10
rand_num = random.randint(num_1, num_2)
print(f'Guess a number from {num_1} ~ {num_2}') 


def random_guess(num, val):
    if num == val:
        return True
    else:
        return False

while True:
    val = int(input("Enter number: "))
    if random_guess(rand_num, val):
        print("You guessed correctly!")
        print("Exiting game")
        print("Exiting game")
        break
    else:
        print("Guess again")

