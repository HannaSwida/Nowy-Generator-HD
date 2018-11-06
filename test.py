import random


def pesel():
    year = random.randint(1930, 2001)

    month = random.randint(1, 12)

    odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
    even_months = (4, 6, 9, 11, 24, 26, 29, 31)

    if month in odd_months:
        day = random.randint(1, 31)

    elif month in even_months:
        day = random.randint(1, 30)
    # this is for february
    else:
        if year % 4 == 0 and year != 1900:
            day = random.randint(1, 29)

        else:
            day = random.randint(1, 28)

    four_random = random.randint(10000, 99999)
    four_random = str(four_random)

    # here comes the equation part, it calculates the last digit

    pierwsza = ('%02d' % (year % 100))
    druga = ('%02d' % month)
    trzecia = ('%02d' % day)
    czwarta = (four_random)

    return pierwsza+druga+trzecia+czwarta


for i in range(50):
    print(pesel())
