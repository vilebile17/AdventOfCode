def day1(data):
    def fix_accumulator(accumulator):
        if accumulator > 99:
            return 0
        elif accumulator < 0:
            return 99
        else:
            return accumulator

    counter = 0
    accumulator = 50

    for line in data:
        for _ in range(int(line[1:])):
            if line == "":
                continue
            elif line[0] == "L":
                accumulator -= 1
                accumulator = fix_accumulator(accumulator)
            elif line[0] == "R":
                accumulator += 1
                accumulator = fix_accumulator(accumulator)
            if accumulator == 0:
                counter += 1
    return counter


def main():
    with open("secret_code", "r") as f:
        file = f.readlines()
    print(day1(file))


main()
