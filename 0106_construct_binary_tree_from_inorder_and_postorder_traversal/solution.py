# LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {val: i for i, val in enumerate(inorder)}
        self.post_index = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = postorder[self.post_index]
            self.post_index -= 1
            mid = index[root_val]
            root = TreeNode(root_val)
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root

        return build(0, len(inorder) - 1)
