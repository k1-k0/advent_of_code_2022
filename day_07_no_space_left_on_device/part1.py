# dict with catalogues and their sizes
import enum


class NodeType(str, enum.Enum):
    file = "file"
    dir = "dir"


class Node:
    def __init__(self, name: str, size: int | None = None, type: NodeType = NodeType.dir):
        self.name: int = name
        self.size: int = size
        self.type: NodeType = type
        self.childs: list[Node] = []
        self.parent: Node | None = None


class Filesystem:
    GO_TO_PARENT: str = ".."
    ROOT: str = "/"

    def __init__(self, root: Node | None = None):
        self.root = root
        self.current = root

    def insert(self, node: Node) -> None:
        node.parent = self.current
        self.current.childs.append(node)

    def cd(self, name: str) -> None:
        if name == self.ROOT:
            if not self.root:
                self.root = Node(self.ROOT, 0)
            self.current = self.root
            return

        if name == self.GO_TO_PARENT:
            self.current = self.current.parent
            return
        
        for child in self.current.childs:
            if child.name == name:
                self.current = child
                return

    def find_dirs_of_given_size(self, limit_size: int) -> list[Node]:
        dir_sizes: list[int] = []

        def find_dir_size(node: Node) -> int:
            current_size: int = node.size
            for child in node.childs:
                if child.type == NodeType.dir.value:
                    size = find_dir_size(child)
                else:
                    size = child.size
                current_size += size
            
            dir_sizes.append(current_size)

            return current_size

        root_size = find_dir_size(self.root)
        dir_sizes.append(root_size)
        
        sum_of_small_size_dir: int = 0
        for size in dir_sizes:
            if size <= limit_size:
                sum_of_small_size_dir += size
        
        return sum_of_small_size_dir


def main():
    filename = "input.txt"
    filesystem: Filesystem = Filesystem()

    with open(filename) as f:
        is_ls: bool = False
        for line in f.readlines():
            if "$ ls" in line:
                is_ls = True
                continue

            elif "$ cd" in line:
                is_ls = False
                to: str = line[5:]
                to = to.rstrip()
                filesystem.cd(to)
                continue

            if is_ls:
                info, name = line.split()
                name = name.rstrip()
                current_node: Node
                if "dir" in info:
                    current_node = Node(name, 0, NodeType.dir)
                else:
                    current_node = Node(name, int(info), NodeType.file)

                filesystem.insert(current_node)

        
        sum = filesystem.find_dirs_of_given_size(100000)
        print(f"Total sum of directories is {sum}")


if __name__ == "__main__":
    main()
