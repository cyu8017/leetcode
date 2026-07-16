# LeetCode 0333 - Largest BST Subtree
# https://leetcode.com/problems/largest-bst-subtree/


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode | None) -> int:
        best = 0

        def dfs(node: TreeNode | None) -> tuple[bool, int, int, int]:
            nonlocal best
            if node is None:
                return True, 10**9, -(10**9), 0

            left_ok, left_min, left_max, left_size = dfs(node.left)
            right_ok, right_min, right_max, right_size = dfs(node.right)

            if left_ok and right_ok and left_max < node.val < right_min:
                size = left_size + right_size + 1
                best = max(best, size)
                return True, min(left_min, node.val), max(right_max, node.val), size

            return False, 0, 0, 0

        dfs(root)
        return best
