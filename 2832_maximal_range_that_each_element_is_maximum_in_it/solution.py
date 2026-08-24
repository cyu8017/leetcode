# LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
# https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            left[i] = st[-1] if st else -1
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            right[i] = st[-1] if st else n
            st.append(i)
        return [right[i] - left[i] - 1 for i in range(n)]
