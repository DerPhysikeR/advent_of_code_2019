import math as m


def calculate_fuel_requirement(mass):
    return int(m.floor(mass / 3)) - 2


def calculate_recursive_fuel_requirement(mass):
    if mass < 9:
        return 0
    additional_fuel = calculate_fuel_requirement(mass)
    return additional_fuel + calculate_recursive_fuel_requirement(additional_fuel)


if __name__ == "__main__":
    with open("input.txt", "r") as stream:
        module_masses = [int(mass) for mass in stream]
    print("Part 1:")
    print(sum(calculate_fuel_requirement(mass) for mass in module_masses))
    print("Part 2:")
    print(sum(calculate_recursive_fuel_requirement(mass) for mass in module_masses))
