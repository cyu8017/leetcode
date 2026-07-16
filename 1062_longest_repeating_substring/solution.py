# LeetCode 1062 - Longest Repeating Substring
# https://leetcode.com/problems/longest-repeating-substring/

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)

        def has_dup(length: int) -> bool:
            seen: set[str] = set()
            for i in range(n - length + 1):
                sub = s[i : i + length]
                if sub in seen:
                    return True
                seen.add(sub)
            return False

        lo, hi, ans = 1, n - 1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_dup(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
