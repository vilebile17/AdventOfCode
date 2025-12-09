# https://adventofcode.com/2025/day/8


class Node(object):
    def __init__(self, coord):
        self.coord = coord
        self.connections = set()

    def __str__(self):
        return f"{self.coord}: {self.connections}"


class Graph(object):
    def __init__(self):
        self.coords = {}  # A dictionary that maps from a coord as a tuple to a Node object
        self.circuit = []

    def add(self, coord):
        self.coords[coord] = Node(coord)

    def add_connection(self, coord1, coord2):
        self.coords[coord1].connections.add(coord2)
        self.coords[coord2].connections.add(coord1)

    def find_all_circuit_lengths(self):
        visited = set()
        results = []
        for coord in self.coords:
            if coord not in visited:
                cool_set = set()
                self.__dfs__(coord, cool_set)
                visited |= cool_set
                results.append(len(cool_set))
        return results

    def find_size_of_circuit(self, coord):
        if len(self.coords[coord].connections) == 0:
            return 0

        cool_set = set()
        self.__dfs__(coord, cool_set)
        return len(cool_set)

    def __dfs__(self, coord, cool_set):
        if coord in cool_set:
            return

        cool_set.add(coord)
        for c in self.coords[coord].connections:
            self.__dfs__(c, cool_set)

    def __str__(self):
        string = ""
        for coord in self.coords:
            string += str(self.coords[coord]) + "\n"
        return string


def get_distance(coord1, coord2):
    return (
        (coord2[0] - coord1[0]) ** 2
        + (coord2[1] - coord1[1]) ** 2
        + (coord2[2] - coord1[2]) ** 2
    ) ** 0.5


def the_wierd_multiplying_thing(lst):
    results = []
    for _ in range(3):
        results.append(max(lst))
        lst.remove(max(lst))
    return results[0] * results[1] * results[2]


def main():
    with open("junction_boxes-D8", "r") as f:
        coords = f.readlines()
    coords = list(
        map(
            lambda x: (int(x[0]), int(x[1]), int(x[2])),
            list(map(lambda x: x.split(","), list(map(lambda x: x[:-1], coords)))),
        )
    )

    graph = Graph()
    for coord in coords:
        graph.add(coord)

    already_added = set()
    for i in range(1000):
        min_so_far = float("inf")
        closest_boxes = ((0, 0, 0), (0, 0, 0))
        for coord1 in coords:
            for coord2 in coords:
                if coord1 != coord2:
                    distance = get_distance(coord1, coord2)
                    if distance < min_so_far and (coord1, coord2) not in already_added:
                        min_so_far = distance
                        closest_boxes = (coord1, coord2)

        graph.add_connection(closest_boxes[0], closest_boxes[1])
        already_added.add(closest_boxes)
        already_added.add((closest_boxes[1], closest_boxes[0]))

        print(f"round {i + 1}/1000")

    r = graph.find_all_circuit_lengths()
    print(the_wierd_multiplying_thing(r))


main()
