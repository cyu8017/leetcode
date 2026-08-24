# LeetCode 2496 - Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            all_digit = True
            val = 0
            for c in s:
                if c < "0" or c > "9":
                    all_digit = False
                    break
                val = val * 10 + (ord(c) - 48)
            if not all_digit:
                val = len(s)
            if val > ans:
                ans = val
        return ans
