# LeetCode 0806 - Number of Lines To Write String
# https://leetcode.com/problems/number-of-lines-to-write-string/

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for ch in s:
            w = widths[ord(ch) - 97]
            if width + w > 100:
                lines += 1
                width = w
            else:
                width += w
        return [lines, width]
