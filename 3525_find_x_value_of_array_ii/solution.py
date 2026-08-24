# LeetCode 3525 - Find X Value of Array II
# https://leetcode.com/problems/find-x-value-of-array-ii/

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = [0] * len(queries)
        for qi, q in enumerate(queries):
            idx, val, start, x = q[0], q[1], q[2], q[3]
            nums[idx] = val
            prod, cnt = 1, 0
            for i in range(start, n):
                prod = prod * (nums[i] % k) % k
                if prod == x:
                    cnt += 1
            ans[qi] = cnt
        return ans
