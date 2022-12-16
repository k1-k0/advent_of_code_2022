
# 1. Use regex -> collect to lists -> revert lists -> use only append/pop
# 2. Line with sequence numbers parse like that: remove spaces -> take last number -> we get count of deques

import re
from collections import defaultdict


SPACE = ""
reg_boxes = re.compile("(\[\w\])|(\s{3}\s?)")
reg_moves = re.compile("\d+")


ContainersMap = dict[int, list[str]]


def parse_boxes_to_dict(boxes: list[str]) -> ContainersMap:
    map: dict[int, list[str]] = defaultdict(list)
    boxes.pop() # remove container numbers

    for line in boxes:
        groups = reg_boxes.findall(line)
        for idx, group in enumerate(groups):
            (container, _) = group
            if container != SPACE:
                map[idx+1].insert(0, re.search('\w', container).group())
        
    return map


def apply_strategy(strategy: list[str], map: ContainersMap) -> None:
    for step in strategy:
        (count, source, destination) = [int(item) for item in re.findall(reg_moves, step)]
        for _ in range(count):
            item = map[source].pop()
            map[destination].append(item)


def print_edge_containers(map: ContainersMap) -> None:
    result: str = ""
    for i in range(1, len(map)+1):
        result += map[i][-1]

    print(result)


def main():
    filename = "input.txt"
    with open(filename) as f:
        boxes: list[str] = []
        strategy: list[str] = []
        is_strategy: bool = False
        for line in f.readlines():
            if is_strategy:
                strategy.append(line)
            else:
                if line == "\n":
                    is_strategy = True
                else:
                    boxes.append(line)

        map = parse_boxes_to_dict(boxes)
        apply_strategy(strategy, map)
        print_edge_containers(map)


if __name__ == "__main__":
    main()
