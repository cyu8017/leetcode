# LeetCode 3090 - Maximum Length Substring With Two Occurrences
# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        cnt = [0] * 26
        for r, ch in enumerate(s):
            idx = ord(ch) - 97
            cnt[idx] += 1
            while cnt[idx] > 2:
                cnt[ord(s[l]) - 97] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
