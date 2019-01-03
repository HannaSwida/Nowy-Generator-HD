import random
import time

header = 'Numer porządkowy samochodu funkcjonariuszy|Długość trasy patrolu|Początek trasy|Koniec trasy|Czas patrolu|Ilość problemów podczas patrolu|Data Patrolu'


YEAR = 365 * 24 * 60 * 60

def get_car_number():
    while True:
        yield random.randint(10, 99)

def date(d):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(d))


def get_data_patrolu():
    while True:
        now = int(time.time())
        start = random.randint(now - 2 * YEAR, now - YEAR)
        yield date(start)


def get_patrol_length():
    while True:
        yield random.randint(10, 20)


def get_patrol_time():
    while True:
        yield random.randint(1, 4)


def get_patrol_issues():
    while True:
        yield random.randint(0, 3)