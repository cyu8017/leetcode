# LeetCode 2593 - Find Score of an Array After Marking All Elements
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        idx = list(range(n))
        idx.sort(key=lambda i: (nums[i], i))
        marked = [False] * n
        ans = 0
        for i in idx:
            if marked[i]:
                continue
            ans += nums[i]
            marked[i] = True
            if i - 1 >= 0:
                marked[i - 1] = True
            if i + 1 < n:
                marked[i + 1] = True
        return ans
