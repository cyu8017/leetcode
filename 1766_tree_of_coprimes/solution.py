class Solution:
    def getCoprimes(self, nums, edges):
        from math import gcd
        adj = [[] for _ in range(len(nums))]
        for a, b in edges:
            adj[a].append(b); adj[b].append(a)
        ans = [-1] * len(nums)
        path = [[] for _ in range(51)]
        def dfs(node, parent, depth):
            best = (-1, -1)
            val = nums[node]
            for d in range(1, 51):
                if gcd(val, d) == 1 and path[d]:
                    cand = path[d][-1]
                    if cand[0] > best[0]:
                        best = cand
            ans[node] = best[1]
            path[val].append((depth, node))
            for nxt in adj[node]:
                if nxt != parent:
                    dfs(nxt, node, depth + 1)
            path[val].pop()
        dfs(0, -1, 0)
        return ans
