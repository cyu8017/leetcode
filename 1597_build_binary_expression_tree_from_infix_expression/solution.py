from typing import List

class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def expTree(self, s: str) -> Node:
        nodes, ops = [], []
        priority = {"+": 1, "-": 1, "*": 2, "/": 2}
        def apply():
            op = ops.pop()
            right, left = nodes.pop(), nodes.pop()
            nodes.append(Node(op, left, right))
        for ch in s:
            if ch.isdigit():
                nodes.append(Node(ch))
            elif ch == "(":
                ops.append(ch)
            elif ch == ")":
                while ops[-1] != "(":
                    apply()
                ops.pop()
            else:
                while ops and ops[-1] != "(" and priority[ops[-1]] >= priority[ch]:
                    apply()
                ops.append(ch)
        while ops:
            apply()
        return nodes[0]
