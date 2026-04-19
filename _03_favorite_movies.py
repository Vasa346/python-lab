#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    first = my_favorite_movies[0:10]
    last = my_favorite_movies[42:57]
    second = my_favorite_movies[12:25]
    second_last = my_favorite_movies[35:40]  # исправлено с 41 на 40
    return first, last, second, second_last

if __name__ == '__main__':
    f, l, s, sl = solve()
    print("Задание 03: Любимые фильмы")
    print(f)
    print(l)
    print(s)
    print(sl)
    print()