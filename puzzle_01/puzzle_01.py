import math as m


def calculate_fuel_requirement(mass):
    return int(m.floor(mass / 3)) - 2


if __name__ == "__main__":
    with open("input.txt", "r") as stream:
        module_masses = [int(mass) for mass in stream]
    print(sum(calculate_fuel_requirement(mass) for mass in module_masses))
