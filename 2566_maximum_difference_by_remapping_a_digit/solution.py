# LeetCode 2566 - Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        def remap(frm: str, to: str) -> int:
            v = 0
            for c in s:
                d = to if c == frm else c
                v = v * 10 + (ord(d) - 48)
            return v

        max_v = num
        for c in s:
            if c != "9":
                max_v = remap(c, "9")
                break
        min_v = remap(s[0], "0")
        return max_v - min_v
