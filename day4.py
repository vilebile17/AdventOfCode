# https://adventofcode.com/2025/day/4


def is_accessable(coords, grid):
    # coords is a tuple (row, column)
    counter = 0
    row = coords[0]
    collumn = coords[1]
    for i in range(collumn - 1, collumn + 2):
        try:
            if grid[row - 1][i] == "@" and row - 1 >= 0 and i >= 0:
                counter += 1
        except:
            continue
    for i in range(collumn - 1, collumn + 2):
        try:
            if grid[row + 1][i] == "@" and row + 1 >= 0 and i >= 0:
                counter += 1
        except:
            continue
    for i in range(collumn - 1, collumn + 2, 2):
        try:
            if grid[row][i] == "@" and row >= 0 and i >= 0:
                counter += 1
        except:
            continue

    if counter < 4:
        return True
    return False


def remove_rolls(grid):
    counter = 0
    old_roll_spots = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and is_accessable((i, j), grid):
                old_roll_spots.append((i, j))
                counter += 1

    for coord in old_roll_spots:
        string = grid[coord[0]]
        grid[coord[0]] = string[: coord[1]] + "." + string[coord[1] + 1 :]

    return counter, len(old_roll_spots) != 0


def main():
    with open("rolls-D4", "r") as f:
        grid = f.readlines()

    counter = 0
    made_a_change = True
    while made_a_change:
        result = remove_rolls(grid)
        counter += result[0]
        made_a_change = result[1]
    print(counter)


main()
