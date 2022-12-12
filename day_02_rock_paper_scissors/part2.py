# Enemy: A - Rock, B - Paper, C - Scissors
# My: X - Rock, Y - Paper, Z - Scissors
# Result: X - Lose, Y - Draw, Z - Win

WIN = 6
DRAW = 3
LOSE = 0

ROCK = 1
PAPER = 2
SCISSORS = 3


def calculate_round_score(round: tuple[str, str]) -> int:
    enemy, my = round

    if enemy == "A":    # rock
        if my == "X":       # Lose
            return LOSE + SCISSORS
        elif my == "Y":     # Draw
            return DRAW + ROCK
        else:               # Win
            return WIN + PAPER 
    elif enemy == "B":  # paper
        if my == "X":       # Lose
            return LOSE + ROCK
        elif my == "Y":     # Draw
            return DRAW + PAPER
        else:               # Win
            return WIN + SCISSORS
    else:               # scissors
        if my == "X":       # Lose
            return LOSE + PAPER
        elif my == "Y":     # Draw
            return DRAW + SCISSORS
        else:               # Win
            return WIN + ROCK


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