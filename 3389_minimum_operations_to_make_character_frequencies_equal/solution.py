# LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/


class Solution:
    def makeStringGood(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        ans = len(s)
        for t in range(1, len(s) + 1):
            pool = 0
            for i in range(26):
                if freq[i] > t:
                    pool += freq[i] - t
            deficit = 0
            for i in range(26):
                if freq[i] < t:
                    deficit += t - freq[i]
            ops = max(pool, deficit)
            if ops < ans:
                ans = ops
        if len(s) < ans:
            ans = len(s)
        return ans
