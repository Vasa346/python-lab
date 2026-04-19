#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    goods = {
        "Лампа": "12345",
        "Стол": "23456",
        "Диван": "34567",
        "Стул": "45678",
    }
    store = {
        "12345": [{"quantity": 27, "price": 42}],
        "23456": [{"quantity": 22, "price": 510}, {"quantity": 32, "price": 520}],
        "34567": [{"quantity": 2, "price": 1200}, {"quantity": 1, "price": 1150}],
        "45678": [
            {"quantity": 50, "price": 100},
            {"quantity": 12, "price": 95},
            {"quantity": 43, "price": 97},
        ],
    }

    lamp_code = goods["Лампа"]
    lamp_qty = store[lamp_code][0]["quantity"]
    lamp_cost = lamp_qty * store[lamp_code][0]["price"]

    table_code = goods["Стол"]
    table_qty = store[table_code][0]["quantity"] + store[table_code][1]["quantity"]
    table_cost = (
        store[table_code][0]["quantity"] * store[table_code][0]["price"]
        + store[table_code][1]["quantity"] * store[table_code][1]["price"]
    )

    sofa_code = goods["Диван"]
    sofa_qty = store[sofa_code][0]["quantity"] + store[sofa_code][1]["quantity"]
    sofa_cost = (
        store[sofa_code][0]["quantity"] * store[sofa_code][0]["price"]
        + store[sofa_code][1]["quantity"] * store[sofa_code][1]["price"]
    )

    chair_code = goods["Стул"]
    chair_qty = (
        store[chair_code][0]["quantity"]
        + store[chair_code][1]["quantity"]
        + store[chair_code][2]["quantity"]
    )
    chair_cost = (
        store[chair_code][0]["quantity"] * store[chair_code][0]["price"]
        + store[chair_code][1]["quantity"] * store[chair_code][1]["price"]
        + store[chair_code][2]["quantity"] * store[chair_code][2]["price"]
    )

    return (
        (lamp_qty, lamp_cost),
        (table_qty, table_cost),
        (sofa_qty, sofa_cost),
        (chair_qty, chair_cost),
    )


if __name__ == "__main__":
    lamp, table, sofa, chair = solve()
    print("Задание 10: Склад")
    print("Лампа -", lamp[0], "шт, стоимость", lamp[1], "руб")
    print("Стол -", table[0], "шт, стоимость", table[1], "руб")
    print("Диван -", sofa[0], "шт, стоимость", sofa[1], "руб")
    print("Стул -", chair[0], "шт, стоимость", chair[1], "руб")
    print()
