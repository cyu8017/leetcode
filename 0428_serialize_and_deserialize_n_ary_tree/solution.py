# LeetCode 0428 - Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/


class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class Codec:
    def encode(self, root: Node | None) -> str:
        if root is None:
            return ""
        parts: list[str] = []
        queue: list[Node] = [root]
        while queue:
            node = queue.pop(0)
            parts.append(str(node.val))
            parts.append(str(len(node.children)))
            for child in node.children:
                parts.append(str(child.val))
                queue.append(child)
        return ",".join(parts)

    def decode(self, data: str) -> Node | None:
        if not data:
            return None
        values = data.split(",")
        index = 0

        def read_root() -> Node:
            nonlocal index
            value = int(values[index])
            child_count = int(values[index + 1])
            index += 2
            node = Node(value, [])
            for _ in range(child_count):
                node.children.append(Node(int(values[index]), []))
                index += 1
            return node

        root = read_root()
        queue: list[Node] = list(root.children)
        while queue:
            node = queue.pop(0)
            value = int(values[index])
            child_count = int(values[index + 1])
            index += 2
            if value != node.val:
                raise ValueError(f"expected node value {node.val}, found {value}")
            for _ in range(child_count):
                child = Node(int(values[index]), [])
                node.children.append(child)
                queue.append(child)
                index += 1
        return root

    serialize = encode
    deserialize = decode
