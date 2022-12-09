
def main() -> None:
    elf_calories: list[int] = []

    with open("input.txt") as f:
        current_calories: list[int] = []
        for line in f.readlines():
            if line == "\n":
                elf_calories.append(sum(current_calories))
                current_calories = []
            else:
                current_calories.append(int(line))

    elf_calories.sort(reverse=True)
    sum_of_top_3: int = sum(elf_calories[:3])
    print(f"The summary calories is {sum_of_top_3} calories!")

if __name__ == '__main__':
    main()