class Solution:
    def longestZigZag(self, root):
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:return (-1,-1)
            l=dfs(node.left);r=dfs(node.right)
            a=l[1]+1;b=r[0]+1;ans=max(ans,a,b)
            return a,b
        dfs(root);return ans
