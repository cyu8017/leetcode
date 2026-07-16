# LeetCode 0337 - House Robber III
# https://leetcode.com/problems/house-robber-iii/


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if node is None:
                return 0, 0

            left_with, left_without = dfs(node.left)
            right_with, right_without = dfs(node.right)

            with_rob = node.val + left_without + right_without
            without_rob = max(left_with, left_without) + max(right_with, right_without)
            return with_rob, without_rob

        return max(dfs(root))
