from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            if bool(node.left) ^ bool(node.right):
                ans.append((node.left or node.right).val)
            dfs(node.left); dfs(node.right)
        dfs(root)
        return ans
