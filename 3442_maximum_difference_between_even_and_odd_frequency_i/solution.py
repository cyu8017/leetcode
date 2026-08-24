# LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/


class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        max_odd, min_even = 0, 10**9
        for f in freq:
            if f == 0:
                continue
            if f % 2 == 1:
                if f > max_odd:
                    max_odd = f
            elif f < min_even:
                min_even = f
        return max_odd - min_even
