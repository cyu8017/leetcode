# LeetCode 2451 - Odd String Difference
# https://leetcode.com/problems/odd-string-difference/

from typing import List


class Solution:
    def oddString(self, words: List[str]) -> str:
        def diff(w: str) -> str:
            b = ""
            for i in range(1, len(w)):
                d = ord(w[i]) - ord(w[i - 1])
                b += chr(d + 128) + ","
            return b

        d0, d1 = diff(words[0]), diff(words[1])
        if d0 == d1:
            for i in range(2, len(words)):
                if diff(words[i]) != d0:
                    return words[i]
        if diff(words[2]) == d0:
            return words[1]
        return words[0]
