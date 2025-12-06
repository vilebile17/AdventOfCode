# https://adventofcode.com/2025/day/6


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def normal_math(operations, nums):
    counter = 0
    operation_list = operations[0]
    for i in range(len(operation_list)):
        if operation_list[i] == "+":
            func = add
        else:
            func = mul

        result = nums[0][i]
        for j in range(1, len(nums)):
            result = func(result, nums[j][i])
        counter += result

    return counter


def main():
    with open("hmwrk-D6", "r") as f:
        lines = f.readlines()

    nums = []
    operations = []
    for line in lines:
        line = line.strip()
        if line[0].isnumeric():
            temp = list(filter(lambda x: x, line.split(" ")))
            nums.append(list(map(lambda x: int(x), temp)))
        else:
            operations.append(list(filter(lambda x: x, line.split(" "))))

    print(normal_math(operations, nums))

    beginning_of_numbers = []
    for i in range(len(lines[4][:-1])):
        if lines[4][i] != " ":
            beginning_of_numbers.append(i)

    end_of_numbers = list(map(lambda x: x - 1, beginning_of_numbers))
    for i in range(1, len(end_of_numbers)):
        end_of_numbers[i - 1] = end_of_numbers[i]
    end_of_numbers[-1] = len(lines[4][:-1])

    nums = []
    for i in range(len(beginning_of_numbers)):
        num_list = []
        for j in range(end_of_numbers[i] - 1, beginning_of_numbers[i] - 1, -1):
            num = ""
            for k in range(4):
                line = lines[k]
                if line[j] != " ":
                    num += line[j]
            num_list.append(int(num))

        if lines[4][beginning_of_numbers[i]] == "+":
            func = add
        else:
            func = mul

        result = num_list[0]
        for i in range(1, len(num_list)):
            result = func(result, num_list[i])
        nums.append(result)

    print(sum(nums))


main()
