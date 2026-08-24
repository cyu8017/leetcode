# LeetCode 3636 - Threshold Majority Queries
# https://leetcode.com/problems/threshold-majority-queries/

from typing import List


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for qi, (l, r, t) in enumerate(queries):
            cnt = {}
            for i in range(l, r + 1):
                cnt[nums[i]] = cnt.get(nums[i], 0) + 1
            best = -1
            best_c = 0
            for v, c in cnt.items():
                if c >= t and (c > best_c or (c == best_c and (best == -1 or v < best))):
                    best_c = c
                    best = v
            ans[qi] = best
        return ans
