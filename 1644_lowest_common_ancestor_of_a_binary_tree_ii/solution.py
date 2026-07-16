class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val,self.left,self.right=val,left,right
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        found=0
        def dfs(node):
            nonlocal found
            if not node: return None
            left,right=dfs(node.left),dfs(node.right)
            if node is p or node is q: found+=1; return node
            return node if left and right else left or right
        ans=dfs(root)
        return ans if found==2 else None
