from model import *
import os.path
import csv
import adres
import random
import osoba
import komisariaty

class Baza(object):
    def __init__(self):
        self.adresy = []
        self.osoby = []
        self.komisariaty = []
        self.funkcjonariusze = []
        self.wystawione_mandaty = []
        self.aresztowania = []

        self._id = 0

    def dump(self, target_directory):
        os.mkdir(target_directory)

        def export(table, lst, columns):
            with open(os.path.join(target_directory, "{}.bulk".format(table)), "w", newline='') as f:
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
        export("Komisariat", self.osoby, [
            lambda x: x.id,
            lambda x: x.nazwa,
            lambda x: x.adres
        ])

        #id nazwa przydzial
        export("Funkcjonariusz", self.funkcjonariusze, [
            lambda x: x.id,
            lambda x: x.nazwa,
            lambda x: x.przydzial
        ])

        #id kwota powod czas osoba_legitymowana miejsce funkcjonariusz
        export("WystawienieMandatu", self.wystawione_mandaty, [
            lambda x: x.id,
            lambda x: x.kwota,
            lambda x: x.powod,
            lambda x: x.czas,
            lambda x: x.osoba_legitymowana,
            lambda x: x.funkcjonariusz
        ])

        #id czas czas_interwenji powod dane_osadzonego funkcjonariusz komisariat
        export("PrzebywanieWAreszcie", self.przebywanie_w_areszcie, [
            lambda x: x.id,
            lambda x: x.czas,
            lambda x: x.czas_interwencji,
            lambda x: x.powod,
            lambda x: x.dane_osadzonego,
            lambda x: x.funkcjonariusz,
            lambda x: x.komisariat
        ])

    def next_id(self):
        self._id += 1
        return self._id

    def generate(self, start_date, end_date):
        def generator_adresu():
            return random.choice(self.adresy)
        # TODO: Tu generujesz wszystko

        # Adresy
        i = 0
        for kraj, miasto, ulica, nr in zip(adres.generator_panstw(), adres.generator_miast(),
                                     adres.generator_ulic(), adres.numer_budynku()):
            self.adresy.append(Adres(self.next_id(), kraj, miasto, ulica, nr))
            i += 1
            if i > 100:
                break
        # Osoby (id imie nazwisko pesel telefon email)
        i = 0
        for imie, nazwisko, pesel, telefon, email in zip(
            osoba.generator_imion(),
            osoba.generator_nazwisk(),
            osoba.generator_peseli(),
            osoba.generator_telefonu(),
            osoba.generator_emaili()
        ):
            self.osoby.append(Osoba(self.next_id(), imie, nazwisko, pesel, telefon, email))
            i += 1
            if i > 100:
                break

        # Komisariat (id nazwa adres)
        i = 0
        for id, nazwa, adres in zip(
            komisariaty.generator_nazwy(),
            generator_adresu()

        ):
            self.komisariaty.append(Komisariat(self.next_id(),nazwa, adres))
            i += 1
            if i > 100:
                break

        # Funkcjonariusz id kwota powod czas osoba_legitymowana miejsce funkcjonariusz
        i = 0
        for id, nazwa, adres in zip(
            funkcjonariusz.generator_nazwy(),
            generator_adresu()

        ):
            self.komisariaty.append(Funkcjonariusz(self.next_id(), on, email))
            i += 1
            if i > 100:
                break
