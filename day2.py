class Bag:
    def __init__(self, cubes_revealed: list):
        self.cubes_revealed = cubes_revealed
        self.min_nb_red = 0
        self.min_nb_blue = 0
        self.min_nb_green = 0

    def parse_cubes_revealed(self):
        for game in self.cubes_revealed:
            if game.get("red"):
                self.min_nb_red = max(self.min_nb_red, game.get("red"))
            if game.get("blue"):
                self.min_nb_blue = max(self.min_nb_blue, game.get("blue"))
            if game.get("green"):
                self.min_nb_green = max(self.min_nb_green, game.get("green"))


def get_input():
    with open("inputs/day2.txt", "r") as file:
        lines = [elt.strip() for elt in file.readlines()]
    return lines


def transform_input(lines):
    output = list()
    for line in lines:
        game = list()
        game_id_str, game_outcome_str = line.split(":")
        game_id = int(game_id_str.split(" ")[1])
        for game_outcome in game_outcome_str.split(";"):
            outcome = dict()
            for cubes in game_outcome.split(", "):
                nb, color = cubes.strip().split(" ")
                outcome[color.strip()] = int(nb)
            game.append(outcome)
        output.append((game_id, game))
    return output


def part1(nb_red, nb_green, nb_blue):
    games = transform_input(get_input())
    s = 0
    for game_id, game in games:
        bag = Bag(game)
        bag.parse_cubes_revealed()
        if (
            bag.min_nb_blue <= nb_blue
            and bag.min_nb_red <= nb_red
            and bag.min_nb_green <= nb_green
        ):
            s += game_id
    return s


def part2():
    games = transform_input(get_input())
    s = 0
    for game_id, game in games:
        bag = Bag(game)
        bag.parse_cubes_revealed()
        s += bag.min_nb_green * bag.min_nb_red * bag.min_nb_blue
    return s


if __name__ == "__main__":
    answer1 = part1(12, 13, 14)
    print(f"Part 1 answer is {answer1}")
    answer2 = part2()
    print(f"Part 2 answer is {answer2}")
