class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def isEvenOddTree(self, root):
        q = [root]; level = 0
        while q:
            prev = float("-inf") if level % 2 == 0 else float("inf"); nxt = []
            for node in q:
                if node.val % 2 == level % 2: return False
                if level % 2 == 0 and node.val <= prev: return False
                if level % 2 and node.val >= prev: return False
                prev = node.val
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            q = nxt; level += 1
        return True
