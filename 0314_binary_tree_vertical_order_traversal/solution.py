# LeetCode 0314 - Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        columns: dict[int, list[int]] = defaultdict(list)
        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
        min_col = max_col = 0
        while queue:
            node, column = queue.popleft()
            min_col = min(min_col, column)
            max_col = max(max_col, column)
            columns[column].append(node.val)
            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))
        return [columns[column] for column in range(min_col, max_col + 1)]
