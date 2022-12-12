# Enemy: A - Rock, B - Paper, C - Scissors
# My: X - Rock, Y - Paper, Z - Scissors

WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3


def calculate_round_score(round: tuple[str, str]) -> int:
    enemy, my = round

    if enemy == "A":    # rock
        if my == "X":       # rock
            return DRAW + ROCK
        elif my == "Y":     # paper
            return WIN + PAPER
        else:               # scissors
            return LOSE + SCISSORS
    elif enemy == "B":  # paper
        if my == "X":       # rock
            return LOSE + ROCK
        elif my == "Y":     # paper
            return DRAW + PAPER
        else:               # scissors
            return WIN + SCISSORS
    else:               # scissors
        if my == "X":       # rock
            return WIN + ROCK
        elif my == "Y":     # paper
            return LOSE + PAPER
        else:               # scissors
            return DRAW + SCISSORS


def calculate_total_score(rounds: list[tuple[str, str]]) -> int:
    total_score: int = 0
    for round in rounds:
        print(round)
        total_score += calculate_round_score(round)
    return total_score


def main() -> None:
    file_name = "input.txt"
    rounds: list(tuple(str, str)) = []
    with open(file=file_name) as f:
        for line in f.readlines():
            rounds.append(tuple(line.split()))
        score = calculate_total_score(rounds)
        print(f"Your final score is {score}")


if __name__ == "__main__":
    main()