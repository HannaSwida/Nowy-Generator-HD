import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(d))


def generator_powodow():
    yield(random.choice(open("Powod_mandat.txt").read().split('\n')))


def generator_kwot():
    yield(random.randint(100, 500))


def generator_dat():
    now = int(time.time())
    data = random.randint(now - 2*YEAR, now-YEAR)
    yield (date(data))


