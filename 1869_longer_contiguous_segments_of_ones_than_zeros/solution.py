# LeetCode 1869 - Longer Contiguous Segments of Ones than Zeros
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_zeros = max_ones = 0
        zeros = ones = 0

        for ch in s:
            if ch == "0":
                zeros += 1
                ones = 0
                max_zeros = max(max_zeros, zeros)
            else:
                ones += 1
                zeros = 0
                max_ones = max(max_ones, ones)

        return max_ones > max_zeros
