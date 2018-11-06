import random
import pesel


def generator_telefonu():
    for x in range(10):
        yield(random.randint(111111111, 999999999))


def generator_peseli():
    for x in range(10):
        if random.randint(1, 100) < 3:
            yield (0)
        else:
            yield(pesel.pesel())


def generator_imion():
    for i in range(5):
        random_line = random.choice(open("imiona.txt").read().split('\n'))
        yield(random_line)

generator_nazwisk = generator_imion
generator_emaili = generator_imion