from typing import List, Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = [] if children is None else children

class Solution:
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        return Node(root.val, [self.cloneTree(child) for child in root.children])
