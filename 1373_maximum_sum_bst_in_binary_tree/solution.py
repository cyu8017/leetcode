class Solution:
    def maxSumBST(self, root):
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:return (True,float('inf'),float('-inf'),0)
            a,lx,lh,ls=dfs(node.left);b,rx,rh,rs=dfs(node.right)
            if a and b and lh<node.val<rx:
                s=ls+rs+node.val;ans=max(ans,s)
                return True,min(lx,node.val),max(rh,node.val),s
            return False,0,0,0
        dfs(root);return ans
