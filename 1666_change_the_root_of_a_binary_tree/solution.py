# LeetCode 1666 - Change the Root of a Binary Tree

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def flipBinaryTree(self, root: "Node", leaf: "Node") -> "Node":
        node = leaf
        while node is not root:
            parent = node.parent
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            original_left = node.left
            node.left = parent
            if original_left is not None:
                node.right = original_left
            node = parent

        def fix_parent(cur, parent):
            if cur is None:
                return
            cur.parent = parent
            fix_parent(cur.left, cur)
            fix_parent(cur.right, cur)

        fix_parent(leaf, None)
        return leaf
