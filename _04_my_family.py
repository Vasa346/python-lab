#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    my_family_height = [
        ["папа", 182],
        ["мама", 168],
        ["я", 175],
        ["бабушка", 160],
        ["дедушка", 178],
    ]
    father_height = my_family_height[0][1]
    total_height = sum(h[1] for h in my_family_height)
    return father_height, total_height


if __name__ == "__main__":
    fh, th = solve()
    print("Задание 04: Моя семья")
    print("Рост отца -", fh, "см")
    print("Общий рост моей семьи -", th, "см")
    print()
