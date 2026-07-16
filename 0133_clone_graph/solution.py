# LeetCode 0133 - Clone Graph
# https://leetcode.com/problems/clone-graph/

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        clones: dict[int, Node] = {}

        def dfs(current: Node) -> Node:
            if current.val in clones:
                return clones[current.val]
            copy = Node(current.val)
            clones[current.val] = copy
            copy.neighbors = [dfs(neighbor) for neighbor in current.neighbors]
            return copy

        return dfs(node)
