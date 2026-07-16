from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        graph = {}

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
            if not node:
                return
            graph.setdefault(node.val, [])
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        queue = deque([(p, 0)])
        seen = {p}
        while queue:
            node, dist = queue.popleft()
            if node == q:
                return dist
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist + 1))
        return -1
