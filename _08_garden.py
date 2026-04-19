#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    garden_set = set(garden)
    meadow_set = set(meadow)

    all_flowers = garden_set | meadow_set
    both = garden_set & meadow_set
    only_garden = garden_set - meadow_set
    only_meadow = meadow_set - garden_set

    return all_flowers, both, only_garden, only_meadow

if __name__ == '__main__':
    a, b, og, om = solve()
    print("Задание 08: Сад и луг")
    print('Все виды цветов:', a)
    print('Растут и в саду, и на лугу:', b)
    print('Растут только в саду:', og)
    print('Растут только на лугу:', om)
    print()