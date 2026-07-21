from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if node is None:
                return 0
            total = dfs(node.left) + dfs(node.right)
            if total == node.val:
                ans += 1
            return total + node.val

        dfs(root)
        return ans
