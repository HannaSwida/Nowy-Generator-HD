from collections import namedtuple

Osoba = namedtuple("Osoba", "id imie nazwisko pesel telefon email")

Adres = namedtuple("Adres", "id kraj miasto ulica numer")

Komisariat = namedtuple("Komisariat", "id nazwa adres")

Funkcjonariusz = namedtuple("Funkcjonariusz", "id stopien dane_osoby miejsce_przydzialu")

WystawienieMandatu = namedtuple("WystawienieMandatu",
    "id kwota powod czas osoba_legitymowana miejsce funkcjonariusz")

PrzebywanieWAreszcie = namedtuple("PrzebywanieWAreszcie",
    "id czas czas_interwencji powod dane_osadzonego funkcjonariusz komisariat")

Patrole = namedtuple("Patrole",
     "numer_porzadkowy dlugosc_trasy poczatek_trasy koniec_trasy czas_patrolu ilosc_problemow dataPatrolu")
