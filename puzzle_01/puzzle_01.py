def calculate_fuel_requirement(mass):
    return mass // 3 - 2


def calculate_recursive_fuel_requirement(mass):
    if mass < 9:
        return 0
    additional_fuel = calculate_fuel_requirement(mass)
    return additional_fuel + calculate_recursive_fuel_requirement(additional_fuel)


def read_module_masses(file_):
    with open(file_, "r") as stream:
        return [int(mass) for mass in stream]


def solve_part_1(module_masses):
    return sum(calculate_fuel_requirement(mass) for mass in module_masses)


def solve_part_2(module_masses):
    return sum(calculate_recursive_fuel_requirement(mass) for mass in module_masses)


if __name__ == "__main__":
    module_masses = read_module_masses("input.txt")
    print(f"Part 1: {solve_part_1(module_masses)}")
    print(f"Part 2: {solve_part_2(module_masses)}")
