# LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = {}

        def build(node, parent):
            if not node:
                return
            if parent:
                g.setdefault(node.val, []).append(parent.val)
                g.setdefault(parent.val, []).append(node.val)
            build(node.left, node)
            build(node.right, node)

        build(root, None)
        ans = 0
        vis = {start}
        q = [(start, 0)]
        while q:
            cur, d = q.pop(0)
            ans = max(ans, d)
            for nxt in g.get(cur, []):
                if nxt not in vis:
                    vis.add(nxt)
                    q.append((nxt, d + 1))
        return ans
