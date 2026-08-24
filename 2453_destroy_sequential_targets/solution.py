# LeetCode 2453 - Destroy Sequential Targets
# https://leetcode.com/problems/destroy-sequential-targets/

from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        cnt = {}
        for x in nums:
            m = x % space
            cnt[m] = cnt.get(m, 0) + 1
        best_cnt = max(cnt.values()) if cnt else 0
        ans = 1000000000
        for key, value in cnt.items():
            if value == best_cnt:
                for x in nums:
                    if x % space == key and x < ans:
                        ans = x
        return ans
