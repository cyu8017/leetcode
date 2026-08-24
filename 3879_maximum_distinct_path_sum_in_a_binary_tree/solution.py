# LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
# https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSum(self, root: Optional[TreeNode]) -> int:
        g: Dict[TreeNode, List[Optional[TreeNode]]] = {}
        vis: Dict[int, bool] = {}

        def dfs(node: Optional[TreeNode], p: Optional[TreeNode]) -> None:
            if not node:
                return
            g[node] = [p, node.left, node.right]
            dfs(node.left, node)
            dfs(node.right, node)

        def dfs2(node: Optional[TreeNode]) -> int:
            if not node or vis.get(node.val) is True:
                return 0
            vis[node.val] = True
            res = node.val
            best = 0
            for nxt in g[node]:
                best = max(best, dfs2(nxt))
            vis[node.val] = False
            return res + best

        g.clear()
        vis.clear()
        dfs(root, None)
        ans = float("-inf")
        for node in g:
            ans = max(ans, dfs2(node))
            vis.clear()
        return int(ans)
