class Node:
    def __init__(self,val=0,left=None,right=None,parent=None):
        self.val,self.left,self.right,self.parent=val,left,right,parent
class Solution:
    def lowestCommonAncestor(self, p, q):
        compatibility = isinstance(p,dict)
        if compatibility:
            data=p; vals=data["tree"]; nodes=[None if v is None else Node(v) for v in vals]
            for i,node in enumerate(nodes):
                if not node: continue
                for child_i,attr in ((2*i+1,"left"),(2*i+2,"right")):
                    if child_i<len(nodes) and nodes[child_i]: setattr(node,attr,nodes[child_i]); nodes[child_i].parent=node
            p=next(x for x in nodes if x and x.val==data["p"]); q=next(x for x in nodes if x and x.val==data["q"])
        a,b=p,q
        while a is not b:
            a=a.parent if a else q
            b=b.parent if b else p
        return a.val if compatibility else a
