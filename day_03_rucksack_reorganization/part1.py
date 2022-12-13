import string


priorities: dict[str, int] = {k: v for (k, v) in zip(string.ascii_lowercase, list(range(1, 27)))}
priorities.update({k: v for (k, v) in zip(string.ascii_uppercase, list(range(27, 53)))})


def find_duplicate_in_rucksack(items: str) -> str:
    half = len(items) // 2
    first_half, second_half = items[:half], items[half:]
    for item in first_half:
        if item in second_half:
            return item


def main():
    filename = "input.txt"
    with open(filename) as f:
        sum_of_priorities: int = 0
        for line in f.readlines():
            duplicate_item: str = find_duplicate_in_rucksack(line)
            priority_of_item: int = priorities.get(duplicate_item)
            sum_of_priorities += priority_of_item
        
        print(f"Summary of priorities of duplicate items is {sum_of_priorities}")


if __name__ == "__main__":
    main()