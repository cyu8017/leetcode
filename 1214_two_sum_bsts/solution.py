class Solution:
    def twoSumBSTs(self, root1: 'TreeNode', root2: 'TreeNode', target: int) -> bool:
        values = set()
        stack = [root1] if root1 else []
        while stack:
            node = stack.pop()
            values.add(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        stack = [root2] if root2 else []
        while stack:
            node = stack.pop()
            if target - node.val in values: return True
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False
