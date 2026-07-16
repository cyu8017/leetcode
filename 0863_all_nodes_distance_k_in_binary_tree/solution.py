# LeetCode 0863 - All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


from collections import defaultdict, deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph: dict[TreeNode, list[TreeNode]] = defaultdict(list)

        def build(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build(node.left, node)
            build(node.right, node)

        build(root, None)
        queue = deque([(target, 0)])
        seen = {target}
        ans: list[int] = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                ans.append(node.val)
                continue
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist + 1))
        return ans
