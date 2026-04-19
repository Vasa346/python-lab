#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    print("Задание 06: Песни")
    violator_songs_list = [
        ["World in My Eyes", 4.86],
        ["Sweetest Perfection", 4.43],
        ["Personal Jesus", 4.56],
        ["Halo", 4.9],
        ["Waiting for the Night", 6.07],
        ["Enjoy the Silence", 4.20],
        ["Policy of Truth", 4.76],
        ["Blue Dress", 4.29],
        ["Clean", 5.83],
    ]
    total_time_list = 0
    for song in violator_songs_list:
        if song[0] in ["Halo", "Enjoy the Silence", "Clean"]:
            total_time_list += song[1]
    print("Три песни звучат", round(total_time_list, 2), "минут")

    violator_songs_dict = {
        "World in My Eyes": 4.76,
        "Sweetest Perfection": 4.43,
        "Personal Jesus": 4.56,
        "Halo": 4.30,
        "Waiting for the Night": 6.07,
        "Enjoy the Silence": 4.6,
        "Policy of Truth": 4.88,
        "Blue Dress": 4.18,
        "Clean": 5.68,
    }
    total_time_dict = (
        violator_songs_dict["Sweetest Perfection"]
        + violator_songs_dict["Policy of Truth"]
        + violator_songs_dict["Blue Dress"]
    )
    print("А другие три песни звучат", round(total_time_dict, 2), "минут")
    print()


if __name__ == "__main__":
    solve()
