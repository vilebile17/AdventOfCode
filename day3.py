# https://adventofcode.com/2025/day/3


def find_largest_two(line):
    max_so_far = float("-inf")
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if int(line[i] + line[j]) > max_so_far:
                max_so_far = int(line[i] + line[j])
    return max_so_far


def find_largest_n(n, line, num_so_far=""):
    digs_left = n - len(num_so_far)
    if digs_left <= 0:
        return int(num_so_far)

    largest_valid_first_dig = float("-inf")
    indices = []
    for i in range(len(line) - digs_left + 1):
        if int(line[i]) > largest_valid_first_dig:
            largest_valid_first_dig = int(line[i])
            indices = [i]
        elif int(line[i]) == largest_valid_first_dig:
            indices.append(i)

    num_so_far += str(largest_valid_first_dig)
    nums = []
    for i in indices:
        nums.append(find_largest_n(n, line[i + 1 :], num_so_far))

    return max([int(num) for num in nums])


def clean_data(line):
    # Removes the nasty \n at the end of a line which ruins the int() conversions
    return line[:-1]


def main():
    with open("joltage-D3", "r") as f:
        lines = f.readlines()
    lines = [clean_data(line) for line in lines]
    print(sum([find_largest_two(line) for line in lines]))
    print(sum([find_largest_n(12, line) for line in lines]))


main()
