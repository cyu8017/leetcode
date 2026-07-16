# LeetCode 1548

class Solution:
    def mostSimilar(self, n, roads, names, targetPath):
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        dp = [((names[node] != targetPath[0]), (node,)) for node in range(n)]
        for i in range(1, len(targetPath)):
            next_dp = []
            for node in range(n):
                cost, path = min(dp[previous] for previous in graph[node])
                next_dp.append((cost + (names[node] != targetPath[i]), path + (node,)))
            dp = next_dp
        return list(min(dp)[1])
