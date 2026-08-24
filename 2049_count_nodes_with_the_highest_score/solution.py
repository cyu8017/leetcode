# LeetCode 2049 - Count Nodes With the Highest Score
# https://leetcode.com/problems/count-nodes-with-the-highest-score/

from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
        size = [0] * n

        def dfs(u: int) -> int:
            size[u] = 1
            for v in children[u]:
                size[u] += dfs(v)
            return size[u]

        dfs(0)
        best = 0
        ans = 0
        for u in range(n):
            score = 1
            for v in children[u]:
                score *= size[v]
            up = n - size[u]
            if up > 0:
                score *= up
            if score > best:
                best = score
                ans = 1
            elif score == best:
                ans += 1
        return ans
