# LeetCode 3685 - Subsequence Sum After Capping Elements
# https://leetcode.com/problems/subsequence-sum-after-capping-elements/

from typing import List


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        sorted_nums = sorted(nums)
        ans = [False] * n
        reach = [False] * (k + 1)
        reach[0] = True
        idx = 0
        for x in range(1, n + 1):
            while idx < n and sorted_nums[idx] <= x:
                v = sorted_nums[idx]
                for s in range(k, v - 1, -1):
                    if reach[s - v]:
                        reach[s] = True
                idx += 1
            tmp = reach[:]
            rem = n - idx
            for s in range(k + 1):
                if not reach[s]:
                    continue
                t = 1
                while t <= rem and s + t * x <= k:
                    tmp[s + t * x] = True
                    t += 1
            ans[x - 1] = tmp[k]
        return ans
