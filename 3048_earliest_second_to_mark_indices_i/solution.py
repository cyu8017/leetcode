# LeetCode 3048 - Earliest Second to Mark Indices I
# https://leetcode.com/problems/earliest-second-to-mark-indices-i/

from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        def ok(t: int) -> bool:
            last = [0] * (n + 1)
            for s in range(t):
                last[changeIndices[s]] = s
            decrement = 0
            marked = 0
            for s in range(t):
                i = changeIndices[s]
                if last[i] == s:
                    if decrement < nums[i - 1]:
                        return False
                    decrement -= nums[i - 1]
                    marked += 1
                else:
                    decrement += 1
            return marked == n

        l = 0
        r = m + 1
        while l < r:
            mid = (l + r) >> 1
            if ok(mid):
                r = mid
            else:
                l = mid + 1
        return -1 if l > m else l
