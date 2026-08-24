# LeetCode 3159 - Find Occurrences of an Element in an Array
# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ids = [i for i, v in enumerate(nums) if v == x]
        ans = [0] * len(queries)
        for qi, i in enumerate(queries):
            if i - 1 < len(ids):
                ans[qi] = ids[i - 1]
            else:
                ans[qi] = -1
        return ans
