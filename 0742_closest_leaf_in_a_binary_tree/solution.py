# LeetCode 0742 - Closest Leaf in a Binary Tree
# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph: dict[int, list[int]] = defaultdict(list)
        leaves: set[int] = set()

        def build(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if not node.left and not node.right:
                leaves.add(node.val)
            # Right first so ties match the sample (e.g. [1,3,2], k=1 -> 2).
            build(node.right, node)
            build(node.left, node)

        build(root, None)
        queue = deque([k])
        seen = {k}
        while queue:
            value = queue.popleft()
            if value in leaves:
                return value
            for neighbor in graph[value]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return -1
