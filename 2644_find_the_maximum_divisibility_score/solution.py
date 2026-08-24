# LeetCode 2644 - Find the Maximum Divisibility Score
# https://leetcode.com/problems/find-the-maximum-divisibility-score/

from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best, best_score = divisors[0], -1
        for d in divisors:
            score = 0
            for x in nums:
                if x % d == 0:
                    score += 1
            if score > best_score or (score == best_score and d < best):
                best_score = score
                best = d
        return best
