# LeetCode 3005 - Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = [0] * 101
        for x in nums:
            cnt[x] += 1
        mx = -1
        ans = 0
        for x in cnt:
            if mx < x:
                mx = x
                ans = x
            elif mx == x:
                ans += x
        return ans
