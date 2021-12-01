from pathlib import Path
from tools import file_to_list
from collections import Counter
from more_itertools import sliding_window


def get_increase_count(lst_ints: list) -> int:
    val_list = list()
    for index, item in enumerate(lst_ints, -1):
        if index == -1:
            continue
        prev_item = lst_ints[index]
        if item > prev_item:
            val_list.append("Increase")
        else:
            val_list.append("Decrease")
    counted = Counter(val_list)
    return counted['Increase']


input_f = Path("input_1.txt")

lst_ints = [int(x) for x in file_to_list(input_f)]

# lst_ints = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

print(f"Output for 1: {get_increase_count(lst_ints)}")


lst_sums = [sum(lst) for lst in sliding_window(lst_ints, 3)]
out = get_increase_count(lst_sums)
print(f"Output for 2: {out}")




