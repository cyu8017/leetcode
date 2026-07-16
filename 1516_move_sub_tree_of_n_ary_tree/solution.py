# LeetCode 1516 - Move Sub-Tree of N-Ary Tree

from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: "Node", p: "Node", q: "Node") -> "Node":
        parent: dict[Node, Node] = {}

        def build(node: Node) -> None:
            for child in node.children:
                parent[child] = node
                build(child)

        build(root)

        if parent.get(p) is q:
            return root

        def is_ancestor(a: Node, b: Node) -> bool:
            cur = b
            while cur in parent:
                cur = parent[cur]
                if cur is a:
                    return True
            return False

        p_parent = parent.get(p)
        q_parent = parent.get(q)

        if is_ancestor(p, q):
            # Detach q first, then put q where p was (or as new root), then attach p under q.
            q_parent.children.remove(q)
            if p_parent is None:
                root = q
            else:
                p_parent.children[p_parent.children.index(p)] = q
            q.children.append(p)
        else:
            if p_parent is None:
                root = q
            else:
                p_parent.children.remove(p)
            q.children.append(p)

        return root
