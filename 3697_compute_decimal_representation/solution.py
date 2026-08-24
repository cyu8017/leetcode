# LeetCode 3697 - Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/

from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        p = 1
        while n > 0:
            v = n % 10
            n //= 10
            if v != 0:
                ans.append(p * v)
            p *= 10
        ans.reverse()
        return ans
