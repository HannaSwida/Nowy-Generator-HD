from model import *
import os.path
import csv
import adres
import random
import osoba
import komisariaty
import funkcjonariusz
import aresztowania
import mandaty
import patrole

class Baza(object):
    def __init__(self):
        self.adresy = []
        self.osoby = []
        self.komisariaty = []
        self.funkcjonariusze = []
        self.wystawione_mandaty = []
        self.aresztowania = []
        self.patrol = []
        self._id = {}

    def dump(self, target_directory):
        try:
            os.mkdir(target_directory)
        except:
            pass

        def export(table, lst, columns):
            with open(os.path.join(target_directory, "{}.bulk".format(table)), "w", newline='') as f:
                writer = csv.writer(f, delimiter='|')
                for i in lst:
                    row = []
                    for c in columns:
                        row.append(c(i))
                    writer.writerow(row)

        def exportCsv(table,lst, columns):
            with open(os.path.join("{}.csv".format(table)), "a", newline='') as f:
                writer = csv.writer(f, delimiter='|')
                for i in lst:
                    row = []
                    for c in columns:
                        row.append(c(i))
                    writer.writerow(row)

        # TODO: Takie cos dla kazdej tabeli
        # id kraj miasto ulica number
        export("Adresy", self.adresy, [
            lambda x: x.id,
            lambda x: x.kraj,
            lambda x: x.miasto,
            lambda x: x.ulica,
            lambda x: x.numer
        ])
        # id imie nazwisko pesel telefon email
        export("Osoby", self.osoby, [
            lambda x: x.id,
            lambda x: x.imie,
            lambda x: x.nazwisko,
            lambda x: x.pesel,
            lambda x: x.telefon,
            lambda x: x.email

        ])
        # id  nazwa adres
        export("Komisariat", self.komisariaty, [
            lambda x: x.id,
            lambda x: x.nazwa,
            lambda x: x.adres.id
        ])

        #id stopien dane_osoby miejsce_przydzialu
        export("Funkcjonariusz", self.funkcjonariusze, [
            lambda x: x.id,
            lambda x: x.stopien,
            lambda x: x.dane_osoby.id,
            lambda x: x.miejsce_przydzialu.id
        ])

        #id kwota powod czas osoba_legitymowana miejsce funkcjonariusz
        export("WystawienieMandatu", self.wystawione_mandaty, [
            lambda x: x.id,
            lambda x: x.kwota,
            lambda x: x.powod,
            lambda x: x.czas,
            lambda x: x.osoba_legitymowana.id,
            lambda x: x.miejsce.id,
            lambda x: x.funkcjonariusz.id
        ])

        #id czas czas_interwenji powod dane_osadzonego funkcjonariusz komisariat
        export("PrzebywanieWAreszcie", self.aresztowania, [
            lambda x: x.id,
            lambda x: x.czas,
            lambda x: x.czas_interwencji,
            lambda x: x.powod,
            lambda x: x.dane_osadzonego.id,
            lambda x: x.funkcjonariusz.id,
            lambda x: x.komisariat.id
        ])
        #numer_porzadkowy, dlugosc_trasy, poczatek__trasy, koniec__trasy, czas_patrolu, ilosc_problemow
        exportCsv("Patrole", self.patrol, [
            lambda x: x.numer_porzadkowy,
            lambda x: x.dlugosc_trasy,
            lambda x: x.poczatek_trasy.miasto+' '+x.poczatek_trasy.ulica+' '+str(x.poczatek_trasy.numer),
            lambda x: x.koniec_trasy.miasto+' '+x.koniec_trasy.ulica+' '+str(x.koniec_trasy.numer),
            lambda x: x.czas_patrolu,
            lambda x: x.ilosc_problemow,
            lambda x: x.dataPatrolu
        ])

    def next_id(self, scope="default"):
        if not scope in self._id: self._id[scope] = 0
        self._id[scope] += 1
        return self._id[scope]

    def generate(self, ilosc_obiektow, start_date, end_date):
        def generator_adresu():
            while True:
                yield random.choice(self.adresy)

        def generator_osob():
            for imie, nazwisko, pesel, telefon, email in zip(
                    osoba.generator_imion(),
                    osoba.generator_nazwisk(),
                    osoba.generator_peseli(),
                    osoba.generator_telefonu(),
                    osoba.generator_emaili()

            ):
                o = Osoba(self.next_id(scope="osoby"), imie, nazwisko, pesel, telefon, email)
                self.osoby.append(o)
                yield o

        def generator_funkcjonariuszy():
            while True:
                yield random.choice(self.funkcjonariusze)

        def generator_komisariatow():
            while True:
                yield random.choice(self.komisariaty)

        # Adresy
        i = 0
        for kraj, miasto, ulica, nr in zip(
                adres.generator_panstw(),
                adres.generator_miast(),
                adres.generator_ulic(),
                adres.numer_budynku()
        ):
            self.adresy.append(Adres(self.next_id(scope="adresy"), kraj, miasto, ulica, nr))
            i += 1
            if i > ilosc_obiektow:
                break

        # Komisariat (id nazwa adres)
        i = 0
        for nazwa, adresy in zip(
            komisariaty.generator_nazwy(),
            generator_adresu()
        ):
            self.komisariaty.append(Komisariat(self.next_id(scope="komisariaty"), nazwa, adresy))
            i += 1
            if i > ilosc_obiektow:
                break

        # id stopien dane_osoby miejsce_przydzialu
        i = 0
        for stopien, dane_osoby, miejsce_przydzialu in zip(
            funkcjonariusz.generator_stopni(),
            generator_osob(),
            generator_komisariatow()
        ):
            self.funkcjonariusze.append(Funkcjonariusz(self.next_id(scope="funkcjonariusze"),
                                                   stopien, dane_osoby, miejsce_przydzialu))
            i += 1
            if i > ilosc_obiektow:
                break
        # id kwota powod czas osoba_legitymowana miejsce funkcjonariusz
        i = 0
        for kwota, powod, czas, osoba_legitymowana, miejsce, _funkcjonariusz in zip(
            mandaty.generator_kwot(),
            mandaty.generator_powodow(),
            mandaty.generator_dat(start_date, end_date),
            generator_osob(),
            generator_adresu(),
            generator_funkcjonariuszy()
        ):
            self.wystawione_mandaty.append(WystawienieMandatu(self.next_id(scope="wystawione_mandaty"), kwota,
                                                       powod, czas, osoba_legitymowana,
                                                       miejsce, _funkcjonariusz))
            i += 1
            if i > ilosc_obiektow:
                break

            # id czas czas_interwenji powod dane_osadzonego funkcjonariusz
        i = 0
        for czas, czas_interwencji, powod, dane_osadzonego, _funkcjonariusz, _komisariat in zip(
            aresztowania.generator_dni(),
            aresztowania.generator_dat(start_date, end_date),
            aresztowania.generator_powodow(),
            generator_osob(),
            generator_funkcjonariuszy(),
            generator_komisariatow()
            ):
            self.aresztowania.append(PrzebywanieWAreszcie(self.next_id(scope="aresztowania"), czas, czas_interwencji,
                                                          powod, dane_osadzonego, _funkcjonariusz,
                                                          _komisariat))
            i += 1
            if i > ilosc_obiektow:
                break

        # Numer porządkowy samochodu funkcjonariuszy|Długość trasy patrolu|Początek trasy|Koniec trasy|Czas patrolu|Ilość problemów podczas patrolu
        i = 0
        for numer_porzadkowy, dlugosc_trasy, poczatek_trasy, koniec_trasy, czas_patrolu, ilosc_problemow, dataPatrolu in zip(
                patrole.get_car_number(),
                patrole.get_patrol_length(),
                generator_adresu(),
                generator_adresu(),
                patrole.get_patrol_time(),
                patrole.get_patrol_issues(),
                patrole.get_data_patrolu()
        ):
            self.patrol.append(Patrole(numer_porzadkowy, dlugosc_trasy, poczatek_trasy, koniec_trasy, czas_patrolu, ilosc_problemow, dataPatrolu))
            i += 1
            if i > ilosc_obiektow:
                break