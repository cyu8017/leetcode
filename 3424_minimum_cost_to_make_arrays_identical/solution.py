# LeetCode 3424 - Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        no_swap = 0
        for i in range(len(arr)):
            no_swap += abs(arr[i] - brr[i])
        a2 = sorted(arr)
        b2 = sorted(brr)
        with_swap = k
        for i in range(len(a2)):
            with_swap += abs(a2[i] - b2[i])
        return no_swap if no_swap < with_swap else with_swap
