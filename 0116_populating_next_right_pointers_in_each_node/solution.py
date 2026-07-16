class Node:
    def __init__(self, val=0, left=None, right=None, next=None): self.val, self.left, self.right, self.next = val, left, right, next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        level=[root]
        while level:
            for i, node in enumerate(level): node.next = level[i+1] if i+1 < len(level) else None
            level=[child for node in level for child in (node.left, node.right) if child]
        return root
