#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    radius = 42

    pi = 3.1415926
    area = pi * radius**2
    print("Задание 01: Площадь круга")
    print(round(area, 4))

    point_1 = (23, 34)
    x1, y1 = point_1
    distance_1 = (x1**2 + y1**2) ** 0.5
    print(distance_1 <= radius)

    point_2 = (30, 30)
    x2, y2 = point_2
    distance_2 = (x2**2 + y2**2) ** 0.5
    print(distance_2 <= radius)
    print()


if __name__ == "__main__":
    solve()
