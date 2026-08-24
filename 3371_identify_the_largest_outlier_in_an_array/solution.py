# LeetCode 3371 - Identify the Largest Outlier in an Array
# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = 0
        freq = {}
        for x in nums:
            total += x
            freq[x] = freq.get(x, 0) + 1
        ans = -2147483648
        for x in nums:
            freq[x] -= 1
            rem = total - x
            if rem % 2 == 0:
                cand = rem // 2
                if freq.get(cand, 0) > 0 and x > ans:
                    ans = x
            freq[x] += 1
        return ans
