import random
from random_words import RandomWords

w = RandomWords()

int_list = []
float_list = []
str_list = []


for _ in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())
