class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def goodNodes(self, root):
        def visit(node, maximum):
            if not node:
                return 0
            good = node.val >= maximum
            maximum = max(maximum, node.val)
            return good + visit(node.left, maximum) + visit(node.right, maximum)
        return visit(root, float("-inf"))
