# LeetCode 1128 - Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        keys = [tuple(sorted(d)) for d in dominoes]
        ans = 0
        for count in Counter(keys).values():
            ans += count * (count - 1) // 2
        return ans
