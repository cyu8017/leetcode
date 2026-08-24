# LeetCode 2109 - Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        b = []
        j = 0
        for i, ch in enumerate(s):
            if j < len(spaces) and spaces[j] == i:
                b.append(" ")
                j += 1
            b.append(ch)
        return "".join(b)
