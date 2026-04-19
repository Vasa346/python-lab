#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io

# Настройка кодировки для корректного вывода в Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Импортируем функции solve из каждого модуля
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

    solve_00()
    solve_01()
    solve_02()
    solve_03()
    solve_04()
    solve_05()
    solve_06()
    solve_07()
    solve_08()
    solve_09()
    solve_10()

    print("=" * 50)
    print("Все задания выполнены!")
    print("=" * 50)


if __name__ == "__main__":
    main()
