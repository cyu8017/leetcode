# LeetCode 2645 - Minimum Additions to Make Valid String
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/


class Solution:
    def addMinimum(self, word: str) -> int:
        ans, expect, i, n = 0, 0, 0, len(word)
        while i < n:
            need = chr(97 + expect)
            if word[i] == need:
                i += 1
            else:
                ans += 1
            expect = (expect + 1) % 3
        ans += (3 - expect) % 3
        return ans
