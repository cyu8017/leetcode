# LeetCode 2259 - Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i, ch in enumerate(number):
            if ch == digit:
                cand = number[:i] + number[i + 1 :]
                if cand > best:
                    best = cand
        return best
