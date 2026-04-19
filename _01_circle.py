#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    radius = 42
    pi = 3.1415926
    area = round(pi * radius**2, 4)

    point_1 = (23, 34)
    x1, y1 = point_1
    inside_1 = (x1**2 + y1**2) ** 0.5 <= radius

    point_2 = (30, 30)
    x2, y2 = point_2
    inside_2 = (x2**2 + y2**2) ** 0.5 <= radius

    return area, inside_1, inside_2


if __name__ == "__main__":
    area, inside_1, inside_2 = solve()
    print("Задание 01: Площадь круга")
    print(area)
    print(inside_1)
    print(inside_2)
    print()
