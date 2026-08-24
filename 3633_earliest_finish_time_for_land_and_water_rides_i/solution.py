# LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        def calc(a1: List[int], t1: List[int], a2: List[int], t2: List[int]) -> int:
            min_end = min(a1[i] + t1[i] for i in range(len(a1)))
            ans = min(max(min_end, a2[i]) + t2[i] for i in range(len(a2)))
            return ans

        return min(
            calc(landStartTime, landDuration, waterStartTime, waterDuration),
            calc(waterStartTime, waterDuration, landStartTime, landDuration),
        )
