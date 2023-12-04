class Card:
    def __init__(self, line):
        self.line = line
        self.card_id, numbers = line.split(":")
        self.winning_numbers, self.numbers = numbers.strip().split("|")
        self.winning_numbers = set(
            [
                int(elt.strip())
                for elt in self.winning_numbers.strip().split(" ")
                if elt.strip()
            ]
        )
        self.numbers = [
            int(elt.strip()) for elt in self.numbers.strip().split(" ") if elt.strip()
        ]

    def get_points(self):
        points = 0
        for nb in self.numbers:
            if nb in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points

    def get_nb_winning_numbers(self):
        nb_winning_numbers = 0
        for nb in self.numbers:
            if nb in self.winning_numbers:
                nb_winning_numbers += 1
        return nb_winning_numbers


def get_input():
    with open("inputs/day4.txt", "r") as f:
        lines = [elt.strip() for elt in f.readlines()]
    return lines


def part1():
    lines = get_input()
    s = 0
    for line in lines:
        card = Card(line)
        s += card.get_points()
    return s


def part2(verbose=False):
    lines = get_input()
    # count the original cards
    nb_cards = {(i + 1): 1 for i in range(len(lines))}
    for idx, line in enumerate(lines):
        card = Card(line)
        nb_of_copies_of_current_card = nb_cards.get(idx + 1)
        nb_of_copies = card.get_nb_winning_numbers()
        if verbose:
            print(f"Card #{idx + 1} has {nb_of_copies} matching numbers")
        for i in range((idx + 1), (idx + 1 + nb_of_copies)):
            if nb_cards.get(i + 1):
                if verbose:
                    print(
                        f"Adding {1 * nb_of_copies_of_current_card} copies to card #{i + 1}"
                    )
                nb_cards[i + 1] += 1 * nb_of_copies_of_current_card
    return sum(nb_cards.values())


if __name__ == "__main__":
    answer1 = part1()
    print(f"Part 1 answer is {answer1}")
    answer2 = part2(verbose=False)
    print(f"Part 2 answer is {answer2}")
