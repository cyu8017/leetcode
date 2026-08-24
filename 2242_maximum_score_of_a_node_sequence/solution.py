# LeetCode 2242 - Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/

from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        top = [[] for _ in range(n)]
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        for i in range(n):
            for v in g[i]:
                top[i].append(v)
                j = len(top[i]) - 1
                while j > 0:
                    if scores[top[i][j]] > scores[top[i][j - 1]]:
                        top[i][j], top[i][j - 1] = top[i][j - 1], top[i][j]
                    j -= 1
                if len(top[i]) > 3:
                    top[i] = top[i][:3]
        ans = -1
        for a, b in edges:
            for c in top[a]:
                if c == b:
                    continue
                for d in top[b]:
                    if d == a or d == c:
                        continue
                    ans = max(ans, scores[a] + scores[b] + scores[c] + scores[d])
        return ans
