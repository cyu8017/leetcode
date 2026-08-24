# LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/


class Solution:
    def maxProduct(self, s: str) -> int:
        def pal_len(mask: int) -> int:
            chars = []
            for i, ch in enumerate(s):
                if mask & (1 << i):
                    chars.append(ch)
            l, r = 0, len(chars) - 1
            while l < r:
                if chars[l] != chars[r]:
                    return 0
                l += 1
                r -= 1
            return len(chars)

        n = len(s)
        best = 0
        total = 1 << n
        for mask1 in range(1, total):
            len1 = pal_len(mask1)
            if len1 == 0:
                continue
            remain = (total - 1) ^ mask1
            mask2 = remain
            while mask2:
                len2 = pal_len(mask2)
                if len2 > 0 and len1 * len2 > best:
                    best = len1 * len2
                mask2 = (mask2 - 1) & remain
        return best
