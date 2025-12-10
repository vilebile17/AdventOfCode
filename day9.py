# https://adventofcode.com/2025/day/9


def find_area(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)


def main():
    with open("red_tiles-D9", "r") as f:
        coords = f.readlines()
    coords = list(map(lambda x: x[:-1], coords))
    coords = list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), coords))

    max_so_far = float("-inf")
    for coord1 in coords:
        for coord2 in coords:
            area = find_area(coord1, coord2)
            if area > max_so_far:
                max_so_far = area

    print(max_so_far)


main()
