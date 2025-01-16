from time import time
from random import random


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1}ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(0, 1002000000):
        i*5

# long_time()


# Excersize
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if (args[0]['valid'] == True):
            return fn(*args, **kwargs)
        else:
            print("authentication failed")
            return 0
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
