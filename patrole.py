import random

header = 'Numer porządkowy samochodu funkcjonariuszy|Długość trasy patrolu|Początek trasy|Koniec trasy|Czas patrolu|Ilość problemów podczas patrolu'

def get_car_number():
    yield random.randint(10, 99)

def get_patrol_length():
    yield random.randint(10, 20)

def get_patrol_time():
    yield random.randint(1, 4)

def get_patrol_issues():
    yield random.randint(0, 3)