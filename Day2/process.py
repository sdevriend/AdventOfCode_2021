from pathlib import Path
from tools import open_file_line_list
input_f = Path("dataset.txt")

test_data = [["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]
lst_input = open_file_line_list(input_f)

instructions = list()
for item in lst_input:
    if item:
        cord_com, cord_pos = item.split()
        instructions.append([cord_com, int(cord_pos)])


stat = {"Horizontal": 0, "Depth": 0}

for cord in instructions:
    if cord[0] == "forward":
        stat["Horizontal"] += cord[1]
    elif cord[0] == "up":
        stat["Depth"] -= cord[1]
    elif cord[0] == "down":
        stat["Depth"] += cord[1]

res = stat["Horizontal"] * stat["Depth"]
print(f"Result for assignment 1 = {res}")

stat_aim = {"Horizontal": 0, "Depth": 0, "Aim": 0,}
for cord in instructions:
    if cord[0] == "forward":
        stat_aim["Horizontal"] += cord[1]
        stat_aim["Depth"] += (cord[1] * stat_aim['Aim'])

    elif cord[0] == "up":
        stat_aim["Aim"] -= cord[1]
    elif cord[0] == "down":
        stat_aim["Aim"] += cord[1]

res2 = stat_aim["Horizontal"] * stat_aim["Depth"]
print(f"Result for assignment 1 = {res2}")