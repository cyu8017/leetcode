# LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        post_index = {v: i for i, v in enumerate(postorder)}

        def build(pre_lo: int, pre_hi: int, post_lo: int, post_hi: int) -> Optional[TreeNode]:
            if pre_lo > pre_hi:
                return None
            root = TreeNode(preorder[pre_lo])
            if pre_lo == pre_hi:
                return root
            left_val = preorder[pre_lo + 1]
            left_post = post_index[left_val]
            left_size = left_post - post_lo + 1
            root.left = build(pre_lo + 1, pre_lo + left_size, post_lo, left_post)
            root.right = build(pre_lo + left_size + 1, pre_hi, left_post + 1, post_hi - 1)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
