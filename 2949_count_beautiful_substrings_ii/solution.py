# LeetCode 2949 - Count Beautiful Substrings II
# https://leetcode.com/problems/count-beautiful-substrings-ii/


def isVowel(c: str) -> bool:
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        x = 1
        while (x * x) % k != 0:
            x += 1
        freq = {(0, 0): 1}
        bal = 0
        vowels = 0
        ans = 0
        for ch in s:
            if isVowel(ch):
                bal += 1
                vowels += 1
            else:
                bal -= 1
            key = (bal, vowels % x)
            f = freq.get(key, 0)
            ans += f
            freq[key] = f + 1
        return ans
