# LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        need = [0] * 26
        required = 0
        for c in word2:
            i = ord(c) - 97
            if need[i] == 0:
                required += 1
            need[i] += 1
        have = [0] * 26
        formed = ans = l = 0
        for r in range(len(word1)):
            c = ord(word1[r]) - 97
            have[c] += 1
            if have[c] == need[c] and need[c] > 0:
                formed += 1
            while formed == required and l <= r:
                ans += len(word1) - r
                c2 = ord(word1[l]) - 97
                if have[c2] == need[c2] and need[c2] > 0:
                    formed -= 1
                have[c2] -= 1
                l += 1
        return ans
