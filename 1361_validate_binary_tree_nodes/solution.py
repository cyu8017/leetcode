class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        indeg=[0]*n
        for x in leftChild+rightChild:
            if x!=-1:
                indeg[x]+=1
                if indeg[x]>1:return False
        roots=[i for i,x in enumerate(indeg) if x==0]
        if len(roots)!=1:return False
        seen=set(); st=roots
        while st:
            u=st.pop()
            if u in seen:return False
            seen.add(u)
            for v in (leftChild[u],rightChild[u]):
                if v!=-1:st.append(v)
        return len(seen)==n
