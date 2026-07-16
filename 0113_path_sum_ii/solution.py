from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None): self.val, self.left, self.right = val, left, right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result=[]
        def visit(node, remaining, path):
            if not node: return
            path.append(node.val)
            if not node.left and not node.right and remaining == node.val: result.append(path[:])
            else: visit(node.left, remaining-node.val, path); visit(node.right, remaining-node.val, path)
            path.pop()
        visit(root, targetSum, []); return result
