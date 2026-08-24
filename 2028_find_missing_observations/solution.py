# LeetCode 2028 - Find Missing Observations
# https://leetcode.com/problems/find-missing-observations/

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remain = mean * (len(rolls) + n) - sum(rolls)
        if remain < n or remain > 6 * n:
            return []
        base_val, extra = divmod(remain, n)
        return [base_val + (1 if i < extra else 0) for i in range(n)]
