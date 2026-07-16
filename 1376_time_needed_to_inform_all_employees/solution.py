class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        children=[[] for _ in range(n)]
        for i,p in enumerate(manager):
            if p!=-1:children[p].append(i)
        def dfs(u):return informTime[u]+max((dfs(v) for v in children[u]),default=0)
        return dfs(headID)
