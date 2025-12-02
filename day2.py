def get_numbers(data):
    lst = []
    ranges = data.split(",")
    for nums in ranges:
        temp = nums.split("-")
        temp[0] = int(temp[0])
        try:
            temp[1] = int(temp[1])
        except Exception as e:
            print(f"Couldn't change {temp[1]} to an int: {e}")
            temp[1] = int(temp[1][:-2])

        lst.append((temp[0], temp[1]))
    return lst


def are_all_the_same(lst):
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            return False
    return True


def is_invalid(n, lst):
    string = str(n)
    for i in range(2, len(string) + 1):
        splits = []
        for j in range(i):
            splits.append(
                string[int(j / i * len(string)) : int((j + 1) / i * len(string))]
            )

        if are_all_the_same(splits):
            lst.append(n)
            return


def main():
    with open("ranges-D2", "r") as f:
        file = f.read()
    nums = get_numbers(file)
    the_big_list = []
    for pair in nums:
        for i in range(pair[0], pair[1] + 1):
            is_invalid(i, the_big_list)
    print(sum(the_big_list))


main()
