import random
import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(d))


def generator_dat(start_date, end_date):
    while True:
        start = random.randint(start_date, end_date)
        yield date(start)


def generator_dni():
    while True:
        yield random.randint(1, 30)


def generator_powodow():
    while True:
        yield(random.choice(open("powod_areszt.txt").read().split('\n')))
