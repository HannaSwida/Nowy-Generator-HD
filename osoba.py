import random





def generator_telefonu():
    for x in range(10):
        yield(random.randint(111111111, 999999999))
