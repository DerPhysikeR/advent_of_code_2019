def to_digits(number):
    return [int(digit) for digit in str(number)]


def has_equal_neighboring_digits(digits):
    return any(digits[i] == digits[i + 1] for i in range(len(digits) - 1))


def monotonic_increasing(digits):
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))


def is_password_valid(password):
    digits = to_digits(password)
    # if len(digits) != 6:
    #     return False
    if not (138241 <= password <= 674034):
        return False
    if not has_equal_neighboring_digits(digits):
        return False
    if not monotonic_increasing(digits):
        return False
    return True


def solve_part_1():
    return sum(is_password_valid(password) for password in range(138241, 674034 + 1))


if __name__ == "__main__":
    print(f"Part 1: {solve_part_1()}")
