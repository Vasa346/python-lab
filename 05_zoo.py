#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    print("Задание 05: Зоопарк")
    zoo = [
        "lion",
        "kangaroo",
        "elephant",
        "monkey",
    ]
    zoo.insert(1, "bear")
    print(zoo)
    birds = [
        "rooster",
        "ostrich",
        "lark",
    ]
    zoo.extend(birds)
    print(zoo)
    zoo.remove("elephant")
    print(zoo)
    lion_cage = zoo.index("lion") + 1
    lark_cage = zoo.index("lark") + 1
    print("Лев сидит в клетке №", lion_cage)
    print("Жаворонок сидит в клетке №", lark_cage)
    print()


if __name__ == "__main__":
    solve()
