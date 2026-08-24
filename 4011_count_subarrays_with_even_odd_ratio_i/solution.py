# LeetCode 4011 - Count Subarrays With Even Odd Ratio I
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

from typing import List


class Solution:
    def countRatioSubarrays(self, nums: List[int], a: int, b: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            y = 0
            for j in range(i, n):
                y += nums[j] % 2
                x = j - i + 1 - y
                if y > 0 and x * b <= y * a:
                    ans += 1
        return ans
