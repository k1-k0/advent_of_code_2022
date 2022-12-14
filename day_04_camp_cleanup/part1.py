

Coordinates = tuple[int, int]


def get_positions(zone: str) -> Coordinates:
    return [int(position) for position in zone.split("-")]


def is_non_effective_work(pair: tuple[str, str]) -> bool:
    (first, second) = pair
    (a, b) = get_positions(first)
    (c, d) = get_positions(second)

    if (a >= c and b <= d) or (c >= a and d <= b):
        return True
    else:
        return False


def main():
    filename = "input.txt"
    with open(filename) as f:
        non_effective_pairs: int = 0
        for line in f.readlines():
            pair: tuple[str, str] = line.split(",")
            if is_non_effective_work(pair):
                non_effective_pairs += 1

        print(f"Total number of useless pair is {non_effective_pairs}")

if __name__ == "__main__":
    main()
