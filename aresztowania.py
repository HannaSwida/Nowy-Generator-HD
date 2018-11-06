import random
import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(d))


def generator_daty():
    while True:
        now = int(time.time())
        start = random.randint(now - 2 * YEAR, now - YEAR)
        yield (date(start))


def generator_dni():
    while True:
        yield random.randint(1, 30)


def generator_powodow():
    while True:
        yield(random.choice(open("powod_areszt.txt").read().split('\n')))
