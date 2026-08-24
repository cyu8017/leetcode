# LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

from typing import List
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = [None] * (m)
        for i in range(m):
            r = startPos[0]
            c = startPos[1]
            cnt = 0
            for j in range(i, m):
                ch = s[j]
                if ch == "L":
                    c -= 1
                elif ch == "R":
                    c += 1
                elif ch == "U":
                    r -= 1
                else:
                    r += 1
                if r < 0 or r >= n or c < 0 or c >= n:
                    break
                cnt += 1
            ans[i] = cnt
        return ans
