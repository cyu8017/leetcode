# LeetCode 2196 - Create Binary Tree From Descriptions
# https://leetcode.com/problems/create-binary-tree-from-descriptions/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        child = set()
        for p, c, isLeft in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if isLeft == 1:
                nodes.get(p).left = nodes.get(c)
            else:
                nodes.get(p).right = nodes.get(c)
            child.add(c)
        for k, v in nodes.items():
            if k not in child:
                return v
        return None
