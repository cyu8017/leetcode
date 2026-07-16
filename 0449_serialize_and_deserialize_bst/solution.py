# LeetCode 0449 - Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        parts: list[str] = []

        def preorder(node: TreeNode | None) -> None:
            if node is None:
                parts.append("#")
                return
            parts.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(parts)

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None
        values = iter(data.split(","))

        def build() -> TreeNode | None:
            token = next(values)
            if token == "#":
                return None
            node = TreeNode(int(token))
            node.left = build()
            node.right = build()
            return node

        return build()
