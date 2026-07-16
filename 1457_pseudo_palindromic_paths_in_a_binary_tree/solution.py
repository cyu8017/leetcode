from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mask):
            if not node:
                return 0
            mask ^= 1 << node.val
            if not node.left and not node.right:
                return int(mask & (mask - 1) == 0)
            return dfs(node.left, mask) + dfs(node.right, mask)
        return dfs(root, 0)
