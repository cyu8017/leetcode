# LeetCode 3844 - Longest Almost Palindromic Substring
# https://leetcode.com/problems/longest-almost-palindromic-substring/

def expand(s: str, l: int, r: int) -> int:
    n = len(s)
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    l1, r1, l2, r2 = l - 1, r, l, r + 1
    while l1 >= 0 and r1 < n and s[l1] == s[r1]:
        l1 -= 1
        r1 += 1
    while l2 >= 0 and r2 < n and s[l2] == s[r2]:
        l2 -= 1
        r2 += 1
    return min(n, max(r1 - l1 - 1, r2 - l2 - 1))


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            ans = max(ans, max(expand(s, i, i), expand(s, i, i + 1)))
        return ans
