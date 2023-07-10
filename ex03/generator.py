#!/usr/bin/env python3

from random import randint


def generator(text, sep=" ", option=None):
    if (not isinstance(text, str) or
            option not in ['shuffle', 'unique', 'ordered', None]):
        yield 'ERROR'
    else:
        lst = text.split(sep)
        if option == 'ordered':
            lst = sorted(lst)
        elif option == 'unique':
            lst = set(lst)
        elif option == 'shuffle':
            new_lst = []
            n = len(lst)
            while(n):
                new_lst.append(lst.pop(randint(0, n - 1)))
                n -= 1
            lst = new_lst
        for word in lst:
            yield word


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print('-' * 30)

for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print('-' * 30)

for word in generator(text, sep=" ", option="ordered"):
    print(word)
print('-' * 30)

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
print('-' * 30)

text = 1.0
for word in generator(text, sep="."):
    print(word)
