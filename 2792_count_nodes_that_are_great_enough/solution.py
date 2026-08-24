# LeetCode 2792 - Count Nodes That Are Great Enough
# https://leetcode.com/problems/count-nodes-that-are-great-enough/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> List[int]:
            nonlocal ans
            if not node:
                return []
            vals = [node.val] + dfs(node.left) + dfs(node.right)
            smaller = sum(1 for v in vals if v < node.val)
            if smaller >= k:
                ans += 1
            return vals

        dfs(root)
        return ans
