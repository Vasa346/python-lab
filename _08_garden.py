#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    print("Задание 08: Сад и луг")
    garden = (
        "ромашка",
        "роза",
        "одуванчик",
        "ромашка",
        "гладиолус",
        "подсолнух",
        "роза",
    )
    meadow = (
        "клевер",
        "одуванчик",
        "ромашка",
        "клевер",
        "мак",
        "одуванчик",
        "ромашка",
    )
    garden_set = set(garden)
    meadow_set = set(meadow)
    print("Все виды цветов:", garden_set | meadow_set)
    print("Растут и в саду, и на лугу:", garden_set & meadow_set)
    print("Растут только в саду:", garden_set - meadow_set)
    print("Растут только на лугу:", meadow_set - garden_set)
    print()


if __name__ == "__main__":
    solve()
