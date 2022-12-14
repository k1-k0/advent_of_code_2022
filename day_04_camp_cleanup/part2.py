

Coordinates = tuple[int, int]


def get_positions(zone: str) -> Coordinates:
    return [int(position) for position in zone.split("-")]


def is_overlap_pair(pair: tuple[str, str]) -> bool:
    (first, second) = pair
    (a, b) = get_positions(first)
    (c, d) = get_positions(second)

    return False if b < c or d < a else True


def main():
    filename = "input.txt"
    with open(filename) as f:
        overlap_pairs: int = 0
        for line in f.readlines():
            pair: tuple[str, str] = line.split(",")
            if is_overlap_pair(pair):
                overlap_pairs += 1

        print(f"Total number of overlap pairs is {overlap_pairs}")

if __name__ == "__main__":
    main()
