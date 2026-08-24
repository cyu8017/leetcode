# LeetCode 2489 - Number of Substrings With Fixed Ratio
# https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/


class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        pref = {0: 1}
        zeros = ones = ans = 0
        for c in s:
            if c == "0":
                zeros += 1
            else:
                ones += 1
            key = zeros * num2 - ones * num1
            ans += pref.get(key, 0)
            pref[key] = pref.get(key, 0) + 1
        return ans
