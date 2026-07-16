class Solution:
    def maximalNetworkRank(self, n, roads):
        degree = [0] * n; edges = set()
        for a, b in roads: degree[a] += 1; degree[b] += 1; edges.add((min(a,b), max(a,b)))
        return max((degree[a] + degree[b] - ((a,b) in edges) for a in range(n) for b in range(a+1,n)), default=0)
