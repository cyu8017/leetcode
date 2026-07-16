class Solution:
    def matrixRankTransform(self, matrix):
        from collections import defaultdict
        m,n=len(matrix),len(matrix[0]); groups=defaultdict(list)
        for i in range(m):
            for j in range(n): groups[matrix[i][j]].append((i,j))
        rank=[0]*(m+n); ans=[[0]*n for _ in range(m)]
        for value in sorted(groups):
            parent={}
            def find(x):
                parent.setdefault(x,x)
                if parent[x]!=x: parent[x]=find(parent[x])
                return parent[x]
            for i,j in groups[value]:
                a,b=find(i),find(m+j); parent[a]=b
            best=defaultdict(int)
            for i,j in groups[value]: best[find(i)]=max(best[find(i)],rank[i],rank[m+j])
            for i,j in groups[value]:
                r=best[find(i)]+1; ans[i][j]=r
            for i,j in groups[value]: rank[i]=max(rank[i],ans[i][j]); rank[m+j]=max(rank[m+j],ans[i][j])
        return ans
