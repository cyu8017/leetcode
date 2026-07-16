# LeetCode 0686 - Repeated String Match
# https://leetcode.com/problems/repeated-string-match/


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeats = (len(b) + len(a) - 1) // len(a)
        built = a * repeats
        if b in built:
            return repeats
        if b in built + a:
            return repeats + 1
        return -1
