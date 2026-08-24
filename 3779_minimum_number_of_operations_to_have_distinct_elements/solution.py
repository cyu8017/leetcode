# LeetCode 3779 - Minimum Number of Operations to Have Distinct Elements
# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in st:
                return i // 3 + 1
            st.add(nums[i])
        return 0
