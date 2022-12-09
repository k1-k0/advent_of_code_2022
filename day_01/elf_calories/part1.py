
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

    max_calories: int = max(elf_calories)
    max_index: int = elf_calories.index(max_calories) + 1
    print(f"The elf #{max_index} has {max_calories} calories!")

if __name__ == '__main__':
    main()