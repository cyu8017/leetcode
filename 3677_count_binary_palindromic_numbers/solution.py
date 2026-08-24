# LeetCode 3677 - Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/


class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 1
        s = ""
        x = n
        while x > 0:
            s += str(x & 1)
            x //= 2
        s = s[::-1]
        L = len(s)
        for length in range(1, L):
            half = (length + 1) // 2
            ans += 1 << (half - 1)
        half = (L + 1) // 2
        prefix = s[:half]
        start = 1 << (half - 1)
        pref_val = 0
        for c in prefix:
            pref_val = (pref_val << 1) | (ord(c) - 48)
        ans += pref_val - start
        pal = prefix
        for i in range(half - 1 - (L % 2), -1, -1):
            pal += prefix[i]
        pval = 0
        for c in pal:
            pval = (pval << 1) | (ord(c) - 48)
        if pval <= n:
            ans += 1
        return ans
