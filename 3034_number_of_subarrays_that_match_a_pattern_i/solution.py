# LeetCode 3034 - Number of Subarrays That Match a Pattern I
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

from typing import List


def fRel(a: int, b: int) -> int:
    if a == b:
        return 0
    return 1 if a < b else -1


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        ans = 0
        for i in range(n - m):
            ok = 1
            k = 0
            while k < m and ok != 0:
                if fRel(nums[i + k], nums[i + k + 1]) != pattern[k]:
                    ok = 0
                k += 1
            ans += ok
        return ans
