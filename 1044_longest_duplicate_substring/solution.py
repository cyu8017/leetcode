# LeetCode 1044 - Longest Duplicate Substring
# https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = (1 << 61) - 1
        BASE = 256
        n = len(s)
        nums = [ord(c) for c in s]

        def search(length: int) -> int:
            if length == 0:
                return 0
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD
            seen = {h: [0]}
            power = pow(BASE, length, MOD)
            for i in range(1, n - length + 1):
                h = (h * BASE - nums[i - 1] * power + nums[i + length - 1]) % MOD
                if h in seen:
                    cur = s[i : i + length]
                    for j in seen[h]:
                        if s[j : j + length] == cur:
                            return i
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return -1

        lo, hi = 0, n - 1
        start = -1
        best_len = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            pos = search(mid)
            if pos >= 0:
                start = pos
                best_len = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[start : start + best_len] if start >= 0 else ""
