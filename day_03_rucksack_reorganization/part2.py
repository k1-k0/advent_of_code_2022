import string


priorities: dict[str, int] = {k: v for (k, v) in zip(string.ascii_lowercase, list(range(1, 27)))}
priorities.update({k: v for (k, v) in zip(string.ascii_uppercase, list(range(27, 53)))})


def find_group_item(group: list[str]) -> str:
    (first, second, third) = sorted(group, key=len, reverse=True)
    for item in first:
        if item in second and item in third:
            return item

def main():
    filename = "input.txt"
    with open(filename) as f:
        sum_of_priorities: int = 0
        group: list[str] = []
        for line in f.readlines():
            group.append(line)
            if len(group) == 3:
                group_item: str = find_group_item(group)
                sum_of_priorities += priorities.get(group_item)
                group = []
        
        print(f"Summary of priorities of duplicate items is {sum_of_priorities}")


if __name__ == "__main__":
    main()