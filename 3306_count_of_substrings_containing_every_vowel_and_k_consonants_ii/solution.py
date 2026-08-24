# LeetCode 3306 - Count of Substrings Containing Every Vowel and K Consonants II
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/

from typing import Dict


def isVowel(c: str) -> bool:
    return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"


def atLeast(word: str, k: int) -> int:
    cnt: Dict[str, int] = {}
    cons = l = ans = 0
    for r in range(len(word)):
        c = word[r]
        if isVowel(c):
            cnt[c] = cnt.get(c, 0) + 1
        else:
            cons += 1
        while len(cnt) == 5 and cons >= k:
            ans += len(word) - r
            c2 = word[l]
            if isVowel(c2):
                nv = cnt[c2] - 1
                if nv == 0:
                    del cnt[c2]
                else:
                    cnt[c2] = nv
            else:
                cons -= 1
            l += 1
    return ans


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return atLeast(word, k) - atLeast(word, k + 1)
