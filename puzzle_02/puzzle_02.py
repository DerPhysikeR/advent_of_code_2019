def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


functions = {1: add, 2: multiply}


def compute(code):
    i = 0
    while i < len(code):
        if code[i] == 99:
            break
        function = functions[code[i]]
        address_1, address_2, result_address = code[i + 1 : i + 4]
        code[result_address] = function(code[address_1], code[address_2])
        i += 4
    return code


def read_input():
    with open("input.txt", "r") as stream:
        return [int(symbol) for symbol in stream.readline().split(",")]


def solve_part_1():
    code = read_input()
    code[1] = 12
    code[2] = 2
    return compute(code)[0]


if __name__ == "__main__":
    print(f"Part 1: {solve_part_1()}")
