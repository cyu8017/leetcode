# LeetCode 3853 - Merge Close Characters
# https://leetcode.com/problems/merge-close-characters/

from typing import Dict


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last: Dict[str, int] = {}
        ans = ""
        for c in s:
            cur = len(ans)
            if c in last and cur - last[c] <= k:
                continue
            ans += c
            last[c] = cur
        return ans
