import random

def generator_nazwy():
       for i in range(5):
            random_line = random.choice(open("komisariaty.txt").read().split('\n'))
            yield (random_line)