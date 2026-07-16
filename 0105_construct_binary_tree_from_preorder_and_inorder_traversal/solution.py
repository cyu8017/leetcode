# LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}
        self.pre_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            mid = index[root_val]
            root = TreeNode(root_val)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
