# LeetCode 2248 - Intersection of Multiple Arrays
# https://leetcode.com/problems/intersection-of-multiple-arrays/

from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = {}
        for arr in nums:
            seen = set()
            for x in arr:
                if x not in seen:
                    seen.add(x)
                    freq[x] = freq.get(x, 0) + 1
        ans = [k for k, v in freq.items() if v == len(nums)]
        ans.sort()
        return ans
