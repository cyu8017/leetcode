# LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def path(node: Optional[TreeNode], target: int, p: List[str]) -> bool:
            if node is None:
                return False
            if node.val == target:
                return True
            p.append("L")
            if path(node.left, target, p):
                return True
            p[-1] = "R"
            if path(node.right, target, p):
                return True
            p.pop()
            return False

        ps, pd = [], []
        path(root, startValue, ps)
        path(root, destValue, pd)
        i = 0
        while i < len(ps) and i < len(pd) and ps[i] == pd[i]:
            i += 1
        return "U" * (len(ps) - i) + "".join(pd[i:])
