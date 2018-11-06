import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(d))


def generator_powodow():
    while True:
        yield(random.choice(open("Powod_mandat.txt").read().split('\n')))


def generator_kwot():
    while True:
        yield(random.randint(100, 500))


def generator_dat():
    while True:
        now = int(time.time())
        data = random.randint(now - 2*YEAR, now-YEAR)
        yield (date(data))


