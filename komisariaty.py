import random


def generator_nazwy():
    while True:
        random_line = random.choice(open("komisariaty.txt").read().split('\n'))
        yield (random_line)