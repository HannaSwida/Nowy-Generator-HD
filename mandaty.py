import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(d))


def generator_powodow():
    while True:
        yield(random.choice(open("Powod_mandat.txt").read().split('\n')))


def generator_kwot():
    while True:
        yield(random.randint(100, 500))


def generator_dat(start_date, end_date):
    while True:
        data = random.randint(start_date, end_date)
        yield date(data)


