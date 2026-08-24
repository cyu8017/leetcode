# LeetCode 2151 - Maximum Good People Based on Statements
# https://leetcode.com/problems/maximum-good-people-based-on-statements/

from typing import List
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        def ok(mask):
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    continue
                for j in range(n):
                    s = statements[i][j]
                    if s == 2:
                        continue
                    goodJ = (mask & (1 << j)) != 0
                    if (s == 1 and not goodJ) or (s == 0 and goodJ):
                        return False
            return True

        ans = 0
        for mask in range((1 << n)):
            if ok(mask):
                bc = 0
                x = mask
                while x:
                    bc += x & 1
                    x >>= 1
                ans = max(ans, bc)
        return ans
