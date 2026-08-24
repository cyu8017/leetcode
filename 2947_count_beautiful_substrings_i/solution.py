# LeetCode 2947 - Count Beautiful Substrings I
# https://leetcode.com/problems/count-beautiful-substrings-i/


def isVowel(c: str) -> bool:
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if isVowel(s[j]):
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
