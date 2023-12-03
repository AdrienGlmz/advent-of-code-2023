def get_input():
    with open("inputs/day3.txt", "r") as f:
        lines = [elt.strip() for elt in f.readlines()]
    return lines


def get_all_symbols(lines):
    all_symbol_positions = dict()
    for i, elt in enumerate(lines):
        for j, char in enumerate(list(elt)):
            if not (48 <= ord(char) <= 57) and char != ".":
                all_symbol_positions[(i, j)] = char
    return all_symbol_positions


def replace_all_symbols_with_dot(elt):
    new_elt = []
    for c in elt:
        if not (48 <= ord(c) <= 57):
            new_elt.append(".")
        else:
            new_elt.append(c)
    return "".join(new_elt)


def get_all_numbers(lines):
    all_number_positions = dict()
    for i, elt in enumerate(lines):
        last_j_index = 0
        elt = replace_all_symbols_with_dot(elt)
        for number_str in elt.split("."):
            cleaned_number_list = []
            for c in number_str:
                if 48 <= ord(c) <= 57:
                    cleaned_number_list.append(c)
            cleaned_number_str = "".join(cleaned_number_list)
            if cleaned_number_str:
                start_idx = elt.find(cleaned_number_str, last_j_index)
                end_idx = start_idx + (len(cleaned_number_str) - 1)
                all_number_positions[(i, start_idx, end_idx)] = int(cleaned_number_str)
                last_j_index = start_idx + 1
    return all_number_positions


def is_match(nb_pos, symbol_pos):
    i1, j_start, j_end = nb_pos
    i2, j2 = symbol_pos
    match = False
    if i1 == i2 and (j2 == j_start - 1 or j2 == j_end + 1):
        # left or right
        match = True
    if i1 == i2 - 1 and (j_start - 1 <= j2 <= j_end + 1):
        # above
        match = True
    if i1 == i2 + 1 and (j_start - 1 <= j2 <= j_end + 1):
        # below
        match = True
    return match


def part1(verbose=False):
    lines = get_input()
    symbol_positions = get_all_symbols(lines)
    number_positions = get_all_numbers(lines)
    s = 0
    for nb_pos, nb in number_positions.items():
        match = False
        for sym_pos, sym in symbol_positions.items():
            if is_match(nb_pos, sym_pos):
                match = True
                if verbose:
                    print(f"MATCH between {nb} and {sym}")
        if not match:
            if verbose:
                print(f"no match for {nb}")
        else:
            s += nb
    return s


def part2():
    lines = get_input()
    symbol_positions = get_all_symbols(lines)
    number_positions = get_all_numbers(lines)
    s = 0
    for sym_pos, sym in symbol_positions.items():
        if sym == "*":
            matches = 0
            prod = 1
            for nb_pos, nb in number_positions.items():
                if is_match(nb_pos, sym_pos):
                    matches += 1
                    prod *= nb
            if matches == 2:
                s += prod
    return s


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
