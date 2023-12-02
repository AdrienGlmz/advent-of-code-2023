MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    **{str(k): k for k in range(10)},
}


def get_input():
    with open("inputs/day1.txt", "r") as file:
        lines = [elt.strip() for elt in file.readlines()]
    return lines


def get_substrings(line: str) -> list:
    substrings = []
    for start_idx in range(len(line) + 1):
        for end_idx in range(start_idx, min(start_idx + 6, len(line) + 1)):
            substrings.append(line[start_idx:end_idx])
    return substrings


def part1():
    lines = get_input()
    numerical_lines = []
    for line in lines:
        numerical_characters = []
        for char in line:
            if 48 <= ord(char) <= 57:
                numerical_characters.append(char)
        numerical_lines.append("".join(numerical_characters))
    return sum([int(f"{elt[0]}{elt[-1]}") for elt in numerical_lines])


def part2():
    lines = get_input()
    numerical_lines = []
    for line in lines:
        numerical_characters = []
        for substring in get_substrings(line):
            if MAPPING.get(substring):
                numerical_characters.append(str(MAPPING.get(substring)))
        numerical_lines.append("".join(numerical_characters))
    return sum([int(f"{elt[0]}{elt[-1]}") for elt in numerical_lines])


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
