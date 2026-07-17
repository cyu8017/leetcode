# LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution:
    def minSwaps(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        if abs(zeros - ones) > 1:
            return -1

        def mismatches(pattern: str) -> int:
            return sum(ch != pattern[i % 2] for i, ch in enumerate(s)) // 2

        if zeros == ones:
            return min(mismatches("01"), mismatches("10"))
        if zeros > ones:
            return mismatches("01")
        return mismatches("10")
