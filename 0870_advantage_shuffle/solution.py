# LeetCode 0870 - Advantage Shuffle
# https://leetcode.com/problems/advantage-shuffle/

from collections import deque


class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        sorted1 = deque(sorted(nums1))
        ans = [0] * len(nums1)
        for i, val in sorted(enumerate(nums2), key=lambda x: -x[1]):
            if sorted1[-1] > val:
                ans[i] = sorted1.pop()
            else:
                ans[i] = sorted1.popleft()
        return ans
