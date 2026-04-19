#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    print("Задание 09: Магазины")
    sweets = {
        "печенье": [
            {"shop": "пятерочка", "price": 9.99},
            {"shop": "ашан", "price": 10.99},
        ],
        "конфеты": [
            {"shop": "магнит", "price": 30.99},
            {"shop": "пятерочка", "price": 32.99},
        ],
        "карамель": [
            {"shop": "магнит", "price": 41.99},
            {"shop": "ашан", "price": 45.99},
        ],
        "пирожное": [
            {"shop": "пятерочка", "price": 59.99},
            {"shop": "магнит", "price": 62.99},
        ],
    }
    for sweet, shop_list in sweets.items():
        print(sweet + ":")
        for shop_info in shop_list:
            print("  ", shop_info["shop"], "-", shop_info["price"])
    print()


if __name__ == "__main__":
    solve()
