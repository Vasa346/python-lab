#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
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


def test_00_distance():
    result = solve_00()
    assert "Moscow" in result
    assert "London" in result
    assert "Paris" in result
    assert result["Moscow"]["London"] == 145.6
    assert result["Paris"]["London"] == 42.43


def test_01_circle():
    area, inside_1, inside_2 = solve_01()
    assert abs(area - 5541.7694) < 0.001
    assert inside_1 == True
    assert inside_2 == False


def test_02_operations():
    r1, r2 = solve_02()
    assert r1 == 9
    assert r2 == 25


def test_03_favorite_movies():
    f, l, s, sl = solve_03()
    assert f == "Терминатор"
    assert l == "Назад в будущее"
    assert s == "Пятый элемент"
    assert sl == "Чужие"


def test_04_my_family():
    fh, th = solve_04()
    assert fh == 182
    assert th == 863


def test_05_zoo():
    z, lc, lac = solve_05()
    assert "bear" in z
    assert "elephant" not in z
    assert lc == 1
    assert lac == 7


def test_06_songs_list():
    tl, td = solve_06()
    assert tl == 14.93
    assert td == 13.49


def test_07_secret():
    w1, w2, w3, w4, w5 = solve_07()
    assert w1 == "в"
    assert w2 == "бане"
    assert w3 == "веник"
    assert w4 == "дороже"
    assert w5 == "денег"


def test_08_garden():
    a, b, og, om = solve_08()
    assert "роза" in a
    assert "ромашка" in b
    assert "гладиолус" in og
    assert "мак" in om


def test_09_shopping():
    sweets = solve_09()
    assert "печенье" in sweets
    assert sweets["печенье"][0]["price"] == 9.99
    assert sweets["конфеты"][0]["shop"] == "магнит"


def test_10_store():
    lamp, table, sofa, chair = solve_10()
    assert lamp == (27, 1134)
    assert table == (54, 27860)
    assert sofa == (3, 3550)
    assert chair == (105, 10311)
