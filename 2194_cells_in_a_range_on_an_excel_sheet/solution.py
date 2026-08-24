# LeetCode 2194 - Cells in a Range on an Excel Sheet
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

from typing import List
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for c in range(ord(s[0]), (ord(s[3])) + 1):
            for r in range(ord(s[1]), (ord(s[4])) + 1):
                ans.append(chr(c) + chr(r))
        return ans
