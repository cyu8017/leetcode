# LeetCode 3185 - Count Pairs That Form a Complete Day II
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt = [0] * 24
        ans = 0
        for x in hours:
            ans += cnt[(24 - x % 24) % 24]
            cnt[x % 24] += 1
        return ans
