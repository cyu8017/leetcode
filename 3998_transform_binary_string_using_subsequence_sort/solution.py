# LeetCode 3998 - Transform Binary String Using Subsequence Sort
# https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

from typing import List


class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == "1" else 0)
        result = [False] * len(strs)
        for i in range(len(strs)):
            left = 0
            right = 0
            ok = True
            for j in range(n):
                left += 1 if strs[i][j] == "1" else 0
                add = 1 if strs[i][j] != "0" else 0
                right = right + add
                if right > prefix[j + 1]:
                    right = prefix[j + 1]
                if left > right:
                    ok = False
                    break
            result[i] = ok and left <= prefix[n] and prefix[n] <= right
        return result
