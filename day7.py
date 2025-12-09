# https://adventofcode.com/2025/day/7


def count_quantum_paths(start_point, lines):
    if len(lines) == 0:
        return 1

    if lines[0][start_point] == "^":
        return count_quantum_paths(start_point - 1, lines[1:]) + count_quantum_paths(
            start_point + 1, lines[1:]
        )
    else:
        return count_quantum_paths(start_point, lines[1:])


def count_splits(lines):
    beams = set()
    for i in range(len(lines[0])):
        if lines[0][i] == "S":
            beams = set([i])

    split_counter = 0
    for line in lines[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == "^":
                split_counter += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams

    return split_counter


def main():
    with open("tachyon_manifolds-D7") as f:
        lines = f.readlines()

    print(count_splits(lines))
    start_point = 0
    for i in range(len(lines[0])):
        if lines[0][i] == "S":
            start_point = i
    print(count_quantum_paths(start_point, lines[1:]))


main()
