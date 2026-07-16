# LeetCode 0429 - N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from collections import deque
from typing import List


class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def levelOrder(self, root: "Node | None") -> List[List[int]]:
        if root is None:
            return []

        result: list[list[int]] = []
        queue: deque[Node] = deque([root])

        while queue:
            level: list[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)

        return result
