# your code goes here
import sys, random, time, csv
import pesel
import osoba
import adres
from baza import Baza

YEAR = 365 * 24 * 60 * 60


def generate_sql(f, table_name, data_type, source):
    for item in source():
        def escape(x):
            if type(x) == str:
                return "\"{}\"".format(x)
            if type(x) == int:
                return str(x)

        item = map(escape, item)
        f.write("INSERT INTO {} ({}) VALUES ({});\n".format(table_name, data_type, ", ".join(item)).encode("windows-1250"))


def generate_sql_osoba(f, table_name, source):
    for item in source():
        f.write("INSERT INTO {} VALUES ({});\n".format(table_name, item).encode("windows-1250"))  # dzieli mi na litery nie slowa, fix


def generate_csv(f, source):
    w = csv.writer(f)
    for x in range(10):
        if random.randint(1, 100) < 3:
            yield (0)
    for i in source():
        w.writerow(i)


def date(d):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(d))


def generator_dat():
    now = int(time.time())
    for i in range(5):
        start = random.randint(now - 2 * YEAR, now - YEAR)
        end = start + random.randint(0, YEAR)
        yield (date(start), date(end))


def main():
    baza = Baza()
    now = int(time.time())
    baza.generate(100, now - 2*YEAR, now - YEAR)
    baza.dump("t1")
    baza.generate(100, now - YEAR, now)
    baza.dump("t2")


    #def generuj_adresy():
    #    # 	Id INTEGER IDENTITY(1,1) PRIMARY KEY,
    #    # 	Kraj VARCHAR(191) NOT NULL,
    #    # 	Miasto VARCHAR(191) NOT NULL,
    #    # 	Ulica VARCHAR(191) NOT NULL,
    #    # 	Numer INTEGER NOT NULL

    #    for i, data in enumerate(zip(adres.generator_panstw(), adres.generator_miast(),
    #                                 adres.generator_ulic(), adres.numer_budynku())):
    #        yield [i] + list(data)
    #        if i > 100:
    #            return

    #generate_sql(sys.stdout, "Adresy",
    #             "Id, Kraj, Miasto, Ulica, Numer",
    #             generuj_adresy)

    # generate_sql_osoba(sys.stdout,  "daty", generator_dat)
    # with f as open("moj.sql"):
    #   generate(f, "daty", generator_dat)
    # generate_csv(sys.stdout, generator_dat)


if __name__ == "__main__":
    main()
