# LeetCode 0076 - Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = Counter(t)
        required = len(need)
        formed = 0
        window: dict[str, int] = {}
        left = 0
        best_len = float("inf")
        best_left = 0
        best_right = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                    best_right = right

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left : best_right + 1]
