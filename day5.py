# https://adventofcode.com/2025/day/5


def is_fresh(ID, ranges):
    for r in ranges:
        nums = r.split("-")
        if int(ID) >= int(nums[0]) and int(ID) <= int(nums[1]):
            return True
    return False


def enumerate_fresh_ingr(ranges, available):
    counter = 0
    for ingredient in available:
        if is_fresh(ingredient, ranges):
            counter += 1
    return counter


def make_range_list(ranges):
    range_lst = []
    for r in ranges:
        lower_bound = int(r.split("-")[0])
        upper_bound = int(r.split("-")[1])
        range_lst.append([lower_bound, upper_bound])
    return sorted(range_lst, key=lambda x: x[0])


def find_all_fresh(old_lst):
    range_lst = [old_lst[0]]
    for i in range(1, len(old_lst)):
        r = old_lst[i]

        # If the ranges overlap
        if r[0] <= range_lst[-1][1]:
            # Check that the range isn't embedded in another
            if r[1] > range_lst[-1][1]:
                range_lst[-1][1] = r[1]
        else:
            range_lst.append(r)

    return range_lst


def main():
    with open("ingredients-D5", "r") as f:
        file = f.read()
    ranges = file.split("\n\n")[0].split("\n")

    available = file.split("\n\n")[1].split("\n")
    available = list(filter(lambda x: x, available))

    print(enumerate_fresh_ingr(ranges, available))
    lst = make_range_list(ranges)
    lst = find_all_fresh(lst)
    print(lst)
    print()
    print(sum(end - start + 1 for (start, end) in lst))


main()
