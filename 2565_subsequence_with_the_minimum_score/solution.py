# LeetCode 2565 - Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        left = [-1] * m
        right = [-1] * m
        j = 0
        i = 0
        while i < n and j < m:
            if s[i] == t[j]:
                left[j] = i
                j += 1
            i += 1
        j = m - 1
        i = n - 1
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                right[j] = i
                j -= 1
            i -= 1
        if m > 0 and left[m - 1] != -1:
            return 0
        ans = m
        for i in range(m):
            if right[i] != -1:
                if i < ans:
                    ans = i
                break
        for i in range(m - 1, -1, -1):
            if left[i] != -1:
                if m - 1 - i < ans:
                    ans = m - 1 - i
                break
        j = 0
        for i in range(m):
            if left[i] == -1:
                break
            while j < m and (right[j] == -1 or right[j] <= left[i]):
                j += 1
            if j < m:
                rem = j - i - 1
                if rem < ans:
                    ans = rem
        return ans
