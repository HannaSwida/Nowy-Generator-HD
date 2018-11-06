import random


def generator_stopni():
    while True:
        yield random.choice(open("stopnie.txt").read().split('\n'))
