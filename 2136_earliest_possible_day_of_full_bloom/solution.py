# LeetCode 2136 - Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        idx = [i for i in range(n)]
        idx.sort(key=lambda a: -growTime[a])
        day = 0
        ans = 0
        for i in idx:
            day += plantTime[i]
            ans = max(ans, day + growTime[i])
        return ans
