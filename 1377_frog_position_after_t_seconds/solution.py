class Solution:
    def frogPosition(self, n, edges, t, target):
        g=[[] for _ in range(n+1)]
        for a,b in edges:g[a].append(b);g[b].append(a)
        def dfs(u,p,time,prob):
            kids=[v for v in g[u] if v!=p]
            if time==t or not kids:return prob if u==target else 0
            return sum(dfs(v,u,time+1,prob/len(kids)) for v in kids)
        return dfs(1,0,0,1.0)
