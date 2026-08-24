# LeetCode 3639 - Minimum Time to Activate String
# https://leetcode.com/problems/minimum-time-to-activate-string/

from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if k > total:
            return -1

        def count_valid(t: int) -> int:
            star = [False] * n
            for i in range(t + 1):
                star[order[i]] = True
            invalid = 0
            i = 0
            while i < n:
                if star[i]:
                    i += 1
                    continue
                j = i
                while j < n and not star[j]:
                    j += 1
                L = j - i
                invalid += L * (L + 1) // 2
                i = j
            return total - invalid

        lo, hi, ans = 0, n - 1, -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            if count_valid(mid) >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
