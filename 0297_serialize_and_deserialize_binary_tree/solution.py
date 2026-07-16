# LeetCode 0297 - Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        values: list[str] = []
        queue: deque[Optional[TreeNode]] = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                values.append("")
            else:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while values and values[-1] == "":
            values.pop()
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue: deque[TreeNode] = deque([root])
        index = 1
        while queue and index < len(values):
            node = queue.popleft()
            if index < len(values) and values[index]:
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if index < len(values) and values[index]:
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
        return root
