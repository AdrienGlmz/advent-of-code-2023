import math


def get_input():
    with open("inputs/day6.txt", "r") as file:
        r = [elt.strip() for elt in file.readlines()]
    return r


def parse_input_part1(lines):
    time = [elt.strip() for elt in lines[0].split(":")[1].split(" ") if elt]
    distance = [elt.strip() for elt in lines[1].split(":")[1].split(" ") if elt]
    output = list()
    for t, d in zip(time, distance):
        output.append({"time": int(t), "distance": int(d)})
    return output


def parse_input_part2(lines):
    time = "".join(lines[0].split(":")[1].replace(" ", ""))
    distance = "".join(lines[1].split(":")[1].replace(" ", ""))
    return [{"time": int(time), "distance": int(distance)}]


def nb_ways_to_win_v2(time, distance):
    # Goal is to find x such as (time - x) * x > distance
    # i.e. - x**2 + time*x - distance > 0
    delta = time**2 - 4 * distance
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        x1 = (time - math.sqrt(delta)) / 2
        n1 = math.ceil(x1) if int(x1) != x1 else x1 + 1
        x2 = (time + math.sqrt(delta)) / 2
        n2 = math.floor(x2) if int(x2) != x2 else x2 - 1
        return int(n2 - n1 + 1)


def part(parse_input_fn):
    product = 1
    parsed_input = parse_input_fn(get_input())
    for game in parsed_input:
        product *= nb_ways_to_win_v2(game["time"], game["distance"])
    return product


if __name__ == "__main__":
    answer1 = part(parse_input_part1)
    print(f"Part 1 answer is {answer1}")
    answer2 = part(parse_input_part2)
    print(f"Part 2 answer is {answer2}")
