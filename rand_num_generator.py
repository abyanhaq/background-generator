import sys
import random

num_1 = int(sys.argv[1])
num_2 = int(sys.argv[2])
rand_num = random.randint(num_1, num_2)
print(f'Guess a number from {num_1} ~ {num_2}')
while True:
    val = int(input("Enter number: "))
    if val == rand_num:
        print("You guessed correctly!")
        print("Exiting game")
        break
    else:
        print("Guess again")
