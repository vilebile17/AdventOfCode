# https://adventofcode.com/2025/day/10

import random


def get_wiring_schemes(string):
    string = string.strip()
    parts = string.split(" ")
    lst = []
    for part in parts:
        lst.append(tuple(part[1:-1].split(",")))
    return lst


def apply_wiring(current_diagram, wiring_scheme):
    for change in wiring_scheme:
        if current_diagram[int(change)] == ".":
            current_diagram = (
                current_diagram[: int(change)]
                + "#"
                + current_diagram[int(change) + 1 :]
            )
        else:
            current_diagram = (
                current_diagram[: int(change)]
                + "."
                + current_diagram[int(change) + 1 :]
            )
    return current_diagram


def create_test_list(depth, wiring_schemes):
    # This is perhaps the most stupid function that I have ever written (but it worked though which is funny)
    lst = []
    for _ in range(depth):
        lst.append(wiring_schemes[random.randint(0, len(wiring_schemes) - 1)])
    return lst


def find_working_button_combo(light_diagram, wiring_schemes, depth=1):
    for _ in range(len(wiring_schemes) ** depth * 10):
        current_diagram = "".join(["." for _ in range(len(light_diagram))])
        test_list = create_test_list(depth, wiring_schemes)
        for thing in test_list:
            current_diagram = apply_wiring(current_diagram, thing)

        if current_diagram == light_diagram:
            return depth
    return find_working_button_combo(light_diagram, wiring_schemes, depth + 1)


def main():
    with open("shiba_inu-D10", "r") as f:
        lines = f.readlines()
    lst = []
    for i in range(len(lines)):
        lst.append([])
        lst[i].append(lines[i].split("]", 1)[0][1:])
        lst[i].append(get_wiring_schemes(lines[i].split("]", 1)[1].split("{")[0]))

    sum = 0
    counter = 0
    for thing in lst:
        counter += 1
        sum += find_working_button_combo(thing[0], thing[1])
        print(f"{counter} / {len(lst)}")
    print(sum)


main()
