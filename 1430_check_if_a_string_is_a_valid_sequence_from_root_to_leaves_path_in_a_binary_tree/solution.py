class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isValidSequence(self, root, arr):
        def visit(node, index):
            if not node or index == len(arr) or node.val != arr[index]:
                return False
            if not node.left and not node.right:
                return index == len(arr) - 1
            return visit(node.left, index + 1) or visit(node.right, index + 1)
        return visit(root, 0)
