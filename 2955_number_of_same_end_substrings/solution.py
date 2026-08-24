# LeetCode 2955 - Number of Same-End Substrings
# https://leetcode.com/problems/number-of-same-end-substrings/

from typing import List


class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pref = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for c in range(26):
                pref[i + 1][c] = pref[i][c]
            pref[i + 1][ord(s[i]) - 97] += 1
        ans = [0] * len(queries)
        for qi, (l, r) in enumerate(queries):
            total = 0
            for c in range(26):
                cnt = pref[r + 1][c] - pref[l][c]
                total += cnt * (cnt + 1) // 2
            ans[qi] = total
        return ans
