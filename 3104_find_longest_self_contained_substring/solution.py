# LeetCode 3104 - Find Longest Self-Contained Substring
# https://leetcode.com/problems/find-longest-self-contained-substring/


class Solution:
    def maxSubstringLength(self, s: str) -> int:
        first = [-1] * 26
        last = [0] * 26
        n = len(s)
        for i, ch in enumerate(s):
            j = ord(ch) - 97
            if first[j] == -1:
                first[j] = i
            last[j] = i
        ans = -1
        for k in range(26):
            i = first[k]
            if i == -1:
                continue
            mx = last[k]
            for j in range(i, n):
                a = first[ord(s[j]) - 97]
                b = last[ord(s[j]) - 97]
                if a < i:
                    break
                mx = max(mx, b)
                if mx == j and j - i + 1 < n:
                    ans = max(ans, j - i + 1)
        return ans
