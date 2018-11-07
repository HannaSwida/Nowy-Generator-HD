import random
import pesel
import mails

def generator_telefonu():
    while True:
        yield(random.randint(111111111, 999999999))


def generator_peseli():
    while True:
        if random.randint(1, 100) < 3:
            yield (0)
        else:
            yield(pesel.pesel())


def generator_imion():
    while True:
        random_line = random.choice(open("imiona.txt").read().split('\n'))
        yield(random_line)

def generator_emaili():
    while True:
        yield(mails.generator_maili())

def generator_nazwisk():
    while True:
        random_line = random.choice(open("nazwisko.txt").read().split('\n'))
        yield(random_line)