# LeetCode 3569 - Maximize Count of Distinct Primes After Split
# https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

from typing import List


class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mx = max(nums)
        for q in queries:
            mx = max(mx, q[1])
        is_p = [False] * (mx + 1)
        for i in range(2, mx + 1):
            is_p[i] = True
        i = 2
        while i * i <= mx:
            if is_p[i]:
                for j in range(i * i, mx + 1, i):
                    is_p[j] = False
            i += 1
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            nums[q[0]] = q[1]
            best = 0
            left = {}
            right = {}
            for v in nums:
                if v <= mx and is_p[v]:
                    right[v] = right.get(v, 0) + 1
            for i in range(len(nums) - 1):
                v = nums[i]
                if v <= mx and is_p[v]:
                    left[v] = left.get(v, 0) + 1
                    c = right[v] - 1
                    if c == 0:
                        del right[v]
                    else:
                        right[v] = c
                best = max(best, len(left) + len(right))
            ans[qi] = best
        return ans
