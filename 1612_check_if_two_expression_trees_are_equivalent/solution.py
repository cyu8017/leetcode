class Node:
    def __init__(self, val="", left=None, right=None):
        self.val, self.left, self.right = val, left, right
def _parse(data):
    if not isinstance(data, str): return data
    vals = data.strip("[]").split(",") if data.strip("[]") else []
    nodes = [None if x == "null" else Node(x) for x in vals]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None); node.right = next(kids, None)
    return nodes[0] if nodes else None
class Solution:
    def checkEquivalence(self, root1, root2):
        from collections import Counter
        def count(node, out):
            if not node: return
            if node.val == "+": count(node.left, out); count(node.right, out)
            else: out[node.val] += 1
        a = Counter(); b = Counter(); count(_parse(root1), a); count(_parse(root2), b)
        return a == b
