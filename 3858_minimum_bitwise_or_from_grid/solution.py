# LeetCode 3858 - Minimum Bitwise Or From Grid
# https://leetcode.com/problems/minimum-bitwise-or-from-grid/

from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        def bit_len(x: int) -> int:
            if x == 0:
                return 0
            n = 0
            while x > 0:
                n += 1
                x >>= 1
            return n

        mx = 0
        for row in grid:
            for x in row:
                mx = max(mx, x)
        m = bit_len(mx)
        ans = 0
        for i in range(m - 1, -1, -1):
            mask = ans | ((1 << i) - 1)
            for row in grid:
                found = False
                for x in row:
                    if (x | mask) == mask:
                        found = True
                        break
                if not found:
                    ans |= 1 << i
                    break
        return ans
