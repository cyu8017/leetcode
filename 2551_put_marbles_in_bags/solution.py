# LeetCode 2551 - Put Marbles in Bags
# https://leetcode.com/problems/put-marbles-in-bags/

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        pair = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair.sort()
        mn = 0
        mx = 0
        for i in range(k - 1):
            mn += pair[i]
            mx += pair[n - 2 - i]
        return mx - mn
