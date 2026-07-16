class Solution:
    def lowestCommonAncestor(self, root, nodes):
        targets=set(nodes)
        if targets and all(not hasattr(x,"val") for x in targets):
            targets=set(targets)
            match=lambda node: node.val in targets
        else:match=lambda node: node in targets
        def dfs(node):
            if not node:return None
            l=dfs(node.left);r=dfs(node.right)
            if match(node) or (l and r):return node
            return l or r
        return dfs(root)
