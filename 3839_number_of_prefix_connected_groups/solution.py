# LeetCode 3839 - Number of Prefix Connected Groups
# https://leetcode.com/problems/number-of-prefix-connected-groups/

from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        cnt = {}
        for w in words:
            if len(w) >= k:
                p = w[:k]
                cnt[p] = cnt.get(p, 0) + 1
        ans = 0
        for v in cnt.values():
            if v > 1:
                ans += 1
        return ans
