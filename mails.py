import random
import string
domeny = ["hotmail.com", "o2.pl", "wp.pl", "eti.gda.pl" , "student.pl", "policja.pl"]
litery = string.ascii_lowercase[:12]


def get_domena(domena):
    return random.choice(domena)


def get_prefix(litery):
    return ''.join(random.choice(litery) for i in range(7))


def generator_maili():
    while True:
        return (get_prefix(litery) + '@' + get_domena(domeny))
