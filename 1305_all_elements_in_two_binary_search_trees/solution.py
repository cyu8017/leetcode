# LeetCode 1305 - All Elements In Two Binary Search Trees

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        a, b = inorder(root1), inorder(root2)
        answer = []
        i = j = 0
        while i < len(a) or j < len(b):
            if j == len(b) or (i < len(a) and a[i] <= b[j]):
                answer.append(a[i]); i += 1
            else:
                answer.append(b[j]); j += 1
        return answer
