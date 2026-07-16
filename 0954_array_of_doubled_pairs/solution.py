# LeetCode 0954 - Array of Doubled Pairs
# https://leetcode.com/problems/array-of-doubled-pairs/

from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] < count[x]:
                return False
            count[2 * x] -= count[x]
        return True
