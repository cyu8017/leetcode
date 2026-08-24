# LeetCode 2612 - Minimum Reverse Operations
# https://leetcode.com/problems/minimum-reverse-operations/

from collections import deque
from typing import List


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ban = set(banned)
        ans = [-1] * n
        ans[p] = 0
        q = deque([(p, 0)])
        while q:
            i, d = q.popleft()
            lo = i - (k - 1)
            if lo < 0:
                lo = 0
            hi = i
            if hi > n - k:
                hi = n - k
            for L in range(lo, hi + 1):
                R = L + k - 1
                ni = L + R - i
                if ni < 0 or ni >= n or ni in ban or ans[ni] != -1:
                    continue
                ans[ni] = d + 1
                q.append((ni, d + 1))
        return ans
