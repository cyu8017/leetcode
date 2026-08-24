# LeetCode 2140 - Solving Questions With Brainpower
# https://leetcode.com/problems/solving-questions-with-brainpower/

from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, (0) - 1, -1):
            pts = questions[i][0]
            brain = questions[i][1]
            next = i + brain + 1
            take = pts + (dp[next] if next < n else 0)
            dp[i] = max(dp[i + 1], take)
        return dp[0]
