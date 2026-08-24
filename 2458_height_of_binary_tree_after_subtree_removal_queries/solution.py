# LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = {}
        level = {}
        level_max = {}

        def dfs(node: Optional[TreeNode], d: int) -> int:
            if not node:
                return -1
            level[node.val] = d
            h = 1 + max(dfs(node.left, d + 1), dfs(node.right, d + 1))
            height[node.val] = h
            arr = level_max.get(d)
            if not arr:
                arr = []
                level_max[d] = arr
            if not arr:
                arr.append(h)
            elif h >= arr[0]:
                if len(arr) == 1:
                    arr.append(arr[0])
                else:
                    arr[1] = arr[0]
                arr[0] = h
            elif len(arr) == 1 or h > arr[1]:
                if len(arr) == 1:
                    arr.append(h)
                else:
                    arr[1] = h
            return h

        dfs(root, 0)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            d = level[q]
            h = height[q]
            top = level_max[d]
            if top[0] == h:
                if len(top) > 1:
                    ans[i] = d + top[1]
                else:
                    ans[i] = d - 1
            else:
                ans[i] = d + top[0]
        return ans
