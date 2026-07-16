# LeetCode 0366 - Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode | None) -> List[List[int]]:
        layers: list[list[int]] = []

        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return -1

            height = max(dfs(node.left), dfs(node.right)) + 1
            while len(layers) <= height:
                layers.append([])
            layers[height].append(node.val)
            return height

        dfs(root)
        return layers
