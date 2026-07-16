from typing import List, Optional

class Node:
    def __init__(self, x=0, left=None, right=None, random=None):
        self.val, self.left, self.right, self.random = x, left, right, random

class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[Node]:
        copies = {}
        def clone(node):
            if node is None:
                return None
            if node not in copies:
                copies[node] = Node(node.val)
                copies[node].left = clone(node.left)
                copies[node].right = clone(node.right)
                copies[node].random = clone(node.random)
            return copies[node]
        return clone(root)
