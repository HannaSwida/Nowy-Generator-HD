# your code goes here
import sys, random, time, csv
import pesel
import osoba
YEAR = 365 * 24 * 60 * 60


def generate_sql(f, table_name, data_type, source):
    for item in source():
        f.write("INSERT INTO {} ({}) VALUES (\'{}\');\n".format(table_name, data_type, ", ".join(map(str, item))))


def generate_sql_osoba(f, table_name, source):
    for item in source():
        f.write("INSERT INTO {} VALUES ({});\n".format(table_name, item)) #dzieli mi na litery nie slowa, fix


def generate_csv(f, source):
    w = csv.writer(f)
    for x in range(10):
        if random.randint(1, 100) < 3:
            yield (0)
    for i in source():
        w.writerow(i)


def date(d):
    return time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(d))


def generator_dat():
    now = int(time.time())
    for i in range(5):
        start = random.randint(now - 2*YEAR, now-YEAR)
        end = start + random.randint(0, YEAR)
        yield (date(start), date(end))


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


def main():
    generate_sql_osoba(sys.stdout,  "daty", generator_dat)
    # with f as open("moj.sql"):
    #   generate(f, "daty", generator_dat)
    generate_csv(sys.stdout, generator_dat)


if __name__ == "__main__":
    main()
