# LeetCode 3987 - Minimum Total Cost to Process All Elements
# https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

from typing import List


class Solution:
    def minimumCost(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        cnt = 0
        cur = k
        for x0 in nums:
            x = x0
            diff = x - cur
            if diff > 0:
                m = (diff + k - 1) // k
                cur += m * k
                cnt += m
            cur -= x
        cnt %= mod
        return (cnt + 1) * cnt // 2 % mod
