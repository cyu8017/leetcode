# LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        st = []
        for i in range(n):
            if not st or nums[i] > nums[st[-1]]:
                st.append(i)
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] > nums[i]:
                j = st.pop()
                if i - j + 1 > ans:
                    ans = i - j + 1
        return ans
