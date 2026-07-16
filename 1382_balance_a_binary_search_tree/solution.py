class Solution:
    def balanceBST(self, root):
        nodes=[]
        def walk(x):
            if x:walk(x.left);nodes.append(x);walk(x.right)
        walk(root)
        def build(l,r):
            if l>=r:return None
            m=(l+r)//2;x=nodes[m];x.left=build(l,m);x.right=build(m+1,r);return x
        return build(0,len(nodes))
