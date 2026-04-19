#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    print("Задание 04: Моя семья")
    my_family = ["папа", "мама", "я", "бабушка", "дедушка"]
    my_family_height = [
        ["папа", 182],
        ["мама", 168],
        ["я", 175],
        ["бабушка", 160],
        ["дедушка", 178],
    ]
    print("Рост отца -", my_family_height[0][1], "см")
    total_height = (
        my_family_height[0][1]
        + my_family_height[1][1]
        + my_family_height[2][1]
        + my_family_height[3][1]
        + my_family_height[4][1]
    )
    print("Общий рост моей семьи -", total_height, "см")
    print()


if __name__ == "__main__":
    solve()
