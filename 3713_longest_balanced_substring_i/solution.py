# LeetCode 3713 - Longest Balanced Substring I
# https://leetcode.com/problems/longest-balanced-substring-i/


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            cnt = [0] * 26
            mx = 0
            v = 0
            for j in range(i, n):
                c = ord(s[j]) - 97
                cnt[c] += 1
                if cnt[c] == 1:
                    v += 1
                mx = max(mx, cnt[c])
                if mx * v == j - i + 1:
                    ans = max(ans, j - i + 1)
        return ans
