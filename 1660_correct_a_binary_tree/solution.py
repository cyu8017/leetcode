class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val,self.left,self.right=val,left,right
class Solution:
    def correctBinaryTree(self, root):
        seen=set()
        def dfs(node):
            if not node:return None
            if node.right in seen:return None
            seen.add(node); node.right=dfs(node.right); node.left=dfs(node.left)
            return node
        return dfs(root)
