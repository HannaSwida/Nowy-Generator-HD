import random
import random
import time
YEAR = 365 * 24 * 60 * 60


def date(d):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(d))

def generator_daty():
    now = int(time.time())
    for i in range(5):
        start = random.randint(now - 2 * YEAR, now - YEAR)
        yield (date(start))


def generator_dni():
    yield random.randint(1, 30)


def generator_powodow():
    yield(random.choice(open("powod_areszt.txt").read().split('\n')))
