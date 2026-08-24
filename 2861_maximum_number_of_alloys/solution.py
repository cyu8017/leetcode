# LeetCode 2861 - Maximum Number of Alloys
# https://leetcode.com/problems/maximum-number-of-alloys/

from typing import List


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        def ok(machines: int) -> bool:
            for comp in composition:
                spend = 0
                for i in range(n):
                    need = machines * comp[i] - stock[i]
                    if need > 0:
                        spend += need * cost[i]
                if spend <= budget:
                    return True
            return False

        lo, hi, ans = 0, 10**9, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
