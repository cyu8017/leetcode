# LeetCode 0919 - Complete Binary Tree Inserter
# https://leetcode.com/problems/complete-binary-tree-inserter/
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue: deque[TreeNode] = deque()
        q: deque[TreeNode] = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            else:
                self.queue.append(node)
                break
            if node.right:
                q.append(node.right)
            else:
                self.queue.append(node)
                break
        self.queue.extend(q)

    def insert(self, val: int) -> int:
        parent = self.queue[0]
        child = TreeNode(val)
        if not parent.left:
            parent.left = child
        else:
            parent.right = child
            self.queue.popleft()
        self.queue.append(child)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
