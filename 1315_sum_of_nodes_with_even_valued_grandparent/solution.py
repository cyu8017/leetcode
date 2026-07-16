# LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent=None, grandparent=None):
            if not node:
                return 0
            add = node.val if grandparent and grandparent.val % 2 == 0 else 0
            return add + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        return dfs(root)
