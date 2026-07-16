# LeetCode 1302 - Deepest Leaves Sum

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while level:
            answer = sum(node.val for node in level)
            level = [child for node in level for child in (node.left, node.right) if child]
        return answer
