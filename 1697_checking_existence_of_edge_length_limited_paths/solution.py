class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        parent=list(range(n))
        def find(x):
            while x!=parent[x]:parent[x]=parent[parent[x]];x=parent[x]
            return x
        ans=[False]*len(queries);edges=sorted(edgeList,key=lambda e:e[2]);i=0
        for limit,p,q,idx in sorted((lim,a,b,j) for j,(a,b,lim) in enumerate(queries)):
            while i<len(edges) and edges[i][2]<limit:
                a,b,_=edges[i];parent[find(a)]=find(b);i+=1
            ans[idx]=find(p)==find(q)
        return ans
