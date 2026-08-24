# LeetCode 3362 - Zero Array Transformation III
# https://leetcode.com/problems/zero-array-transformation-iii/

from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda a: a[0])
        h = []
        n = len(nums)
        diff = [0] * (n + 1)
        j = 0
        used = 0
        cur = 0
        for i in range(n):
            cur += diff[i]
            while j < len(queries) and queries[j][0] == i:
                h.append(queries[j][1])
                j += 1
            while cur < nums[i]:
                if not h:
                    return -1
                h.sort(reverse=True)
                if h[0] < i:
                    return -1
                r = h.pop(0)
                cur += 1
                diff[r + 1] -= 1
                used += 1
        return len(queries) - used
