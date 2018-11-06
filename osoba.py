import random



def generator_miast():
    for x in range(10):
        if random.randint(1, 100) < 30:
            yield(random.choice(open("miasta.txt").read().split('\n')))
        else:
            yield("Gdańsk")


def generator_telefonu():
    for x in range(10):
        yield(random.randint(111111111, 999999999))


def generator_ulic():
    yield(random.choice(open("nazwyulic.txt").read().split('\n')))


def numer_ulicy():
    yield(random.randint(1, 400))
