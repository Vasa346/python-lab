#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from _00_distance import solve as solve_00
from _01_circle import solve as solve_01
from _02_operations import solve as solve_02
from _03_favorite_movies import solve as solve_03
from _04_my_family import solve as solve_04
from _05_zoo import solve as solve_05
from _06_songs_list import solve as solve_06
from _07_secret import solve as solve_07
from _08_garden import solve as solve_08
from _09_shopping import solve as solve_09
from _10_store import solve as solve_10


def main():
    print("=" * 50)
    print("Лабораторная работа №1 - Верхнеуровневый модуль")
    print("=" * 50)
    print()

    print("Задание 00: Расстояния между городами")
    print(solve_00())
    print()

    print("Задание 01: Площадь круга")
    area, inside_1, inside_2 = solve_01()
    print(area)
    print(inside_1)
    print(inside_2)
    print()

    print("Задание 02: Операции")
    r1, r2 = solve_02()
    print(r1)
    print(r2)
    print()

    print("Задание 03: Любимые фильмы")
    f, l, s, sl = solve_03()
    print(f)
    print(l)
    print(s)
    print(sl)
    print()

    print("Задание 04: Моя семья")
    fh, th = solve_04()
    print("Рост отца -", fh, "см")
    print("Общий рост моей семьи -", th, "см")
    print()

    print("Задание 05: Зоопарк")
    z, lc, lac = solve_05()
    print(z)
    print("Лев сидит в клетке №", lc)
    print("Жаворонок сидит в клетке №", lac)
    print()

    print("Задание 06: Песни")
    tl, td = solve_06()
    print("Три песни звучат", tl, "минут")
    print("А другие три песни звучат", td, "минут")
    print()

    print("Задание 07: Секретное сообщение")
    w1, w2, w3, w4, w5 = solve_07()
    print(w1, w2, w3, w4, w5)
    print()

    print("Задание 08: Сад и луг")
    a, b, og, om = solve_08()
    print("Все виды цветов:", a)
    print("Растут и в саду, и на лугу:", b)
    print("Растут только в саду:", og)
    print("Растут только на лугу:", om)
    print()

    print("Задание 09: Магазины")
    sweets = solve_09()
    for sweet, shop_list in sweets.items():
        print(sweet + ":")
        for shop_info in shop_list:
            print("  ", shop_info["shop"], "-", shop_info["price"])
    print()

    print("Задание 10: Склад")
    lamp, table, sofa, chair = solve_10()
    print("Лампа -", lamp[0], "шт, стоимость", lamp[1], "руб")
    print("Стол -", table[0], "шт, стоимость", table[1], "руб")
    print("Диван -", sofa[0], "шт, стоимость", sofa[1], "руб")
    print("Стул -", chair[0], "шт, стоимость", chair[1], "руб")
    print()

    print("=" * 50)
    print("Все задания выполнены!")
    print("=" * 50)


if __name__ == "__main__":
    main()
