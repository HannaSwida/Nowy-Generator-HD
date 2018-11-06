import random

def generator_ulic():
    while True:
        yield random.choice(open("nazwyulic.txt").read().split('\n'))


def numer_budynku():
    while True:
        yield random.randint(1, 400)


def generator_miast():
    while True:
        if random.randint(1, 100) < 30:
            yield random.choice(open("miasta.txt").read().split('\n'))
        else:
            yield "Gdańsk"


def generator_panstw():
    while True:
        if random.randint(1, 100) < 3:
            yield random.choice(open("panstwa.txt").read().split('\n'))
        else:
            yield "Polska"
