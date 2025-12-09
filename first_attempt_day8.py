# https://adventofcode.com/2025/day/8


def get_distance(coord1, coord2):
    return (
        (coord2[0] - coord1[0]) ** 2
        + (coord2[1] - coord1[1]) ** 2
        + (coord2[2] - coord1[2]) ** 2
    ) ** 0.5


def print_circuit_lengths(circuits):
    string = ""
    for circuit in circuits:
        string += f"{len(circuit)}, "
    print(string)


def connect_circuits(circuits):
    for circuit1 in circuits:
        for circuit2 in circuits:
            if circuit1 != circuit2:
                for coord in circuit1:
                    if coord in circuit2:
                        circuit1 = circuit1.union(circuit2)
                        circuits.remove(circuit2)
                        return connect_circuits(circuits)
    return circuits


def main():
    with open("junction_boxes-D8", "r") as f:
        coords = f.readlines()
    coords = list(
        map(
            lambda x: (int(x[0]), int(x[1]), int(x[2])),
            list(map(lambda x: x.split(","), list(map(lambda x: x[:-1], coords)))),
        )
    )

    already_added = []
    circuits = []
    for _ in range(10):
        min_so_far = float("inf")
        closest_boxes = ((0, 0, 0), (0, 0, 0))
        for coord1 in coords:
            for coord2 in coords:
                if coord1 != coord2:
                    if (
                        get_distance(coord1, coord2) < min_so_far
                        and (coord1, coord2) not in already_added
                    ):
                        min_so_far = get_distance(coord1, coord2)
                        closest_boxes = (coord1, coord2)

        added = False
        for circuit in circuits:
            if closest_boxes[0] in circuit:
                circuit.add(closest_boxes[1])
                added = True
            elif closest_boxes[1] in circuit:
                circuit.add(closest_boxes[0])
                added = True

        if not added:
            circuits.append(set((closest_boxes[0], closest_boxes[1])))

        already_added.append(closest_boxes)
        already_added.append(
            (closest_boxes[1], closest_boxes[0])
        )  # The reverse of the first append

    connect_circuits(circuits)
    print(circuits)
    print_circuit_lengths(circuits)


main()
