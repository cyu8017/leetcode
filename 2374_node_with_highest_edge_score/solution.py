# LeetCode 2374 - Node With Highest Edge Score
# https://leetcode.com/problems/node-with-highest-edge-score/

from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        for i in range(n):
            score[edges[i]] += i
        ans = 0
        for i in range(1, n):
            if score[i] > score[ans]:
                ans = i
        return ans
