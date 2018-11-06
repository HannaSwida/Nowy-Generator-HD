import random
import string
domeny = ["hotmail.com", "o2.pl", "wp.pl", "eti.gda.pl" , "student.pl", "policja.pl"]
litery = string.ascii_lowercase[:12]


def get_domena(domena):
    return random.choice(domena)


def get_prefix(litery, length):
    return ''.join(random.choice(litery) for i in range(length))


def generator_maili(length):
    while True:
        yield (get_prefix(litery, length) + '@' + get_domena(domeny))
