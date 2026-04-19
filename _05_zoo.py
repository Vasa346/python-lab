#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    zoo = ["lion", "kangaroo", "elephant", "monkey"]
    zoo.insert(1, "bear")
    birds = ["rooster", "ostrich", "lark"]
    zoo.extend(birds)
    zoo.remove("elephant")
    lion_cage = zoo.index("lion") + 1
    lark_cage = zoo.index("lark") + 1
    return zoo, lion_cage, lark_cage


if __name__ == "__main__":
    z, lc, lac = solve()
    print("Задание 05: Зоопарк")
    print(z)
    print("Лев сидит в клетке №", lc)
    print("Жаворонок сидит в клетке №", lac)
    print()
