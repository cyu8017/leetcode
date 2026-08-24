# LeetCode 2265 - Count Nodes Equal to Average of Subtree
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal ans
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            total = ls + rs + node.val
            cnt = lc + rc + 1
            if total // cnt == node.val:
                ans += 1
            return total, cnt

        dfs(root)
        return ans
