from collections import namedtuple

Osoba = namedtuple("Osoba", "id imie nazwisko pesel telefon email")

Adres = namedtuple("Adres", "id kraj miasto ulica number")

Komisariat = namedtuple("Komisariat", "id nazwa adres")

Funkcjonariusz = namedtuple("Funkjonariusz", "id stopien dane_osoby miejsce_przydzialu")

WystawienieMandatu = namedtuple("WystawienieMandatu",
    "id kwota powod czas osoba_legitymowana miejsce funkcjonariusz")

PrzebywanieWAreszcie = namedtuple("PrzebywanieWAreszcie",
    "id czas czas_interwenji powod dane_osadzonego funkcjonariusz komisariat")
