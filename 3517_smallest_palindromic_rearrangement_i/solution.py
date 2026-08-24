# LeetCode 3517 - Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        t = ""
        ch = ""
        for i in range(26):
            c = chr(97 + i)
            v = cnt[i] // 2
            t += c * v
            cnt[i] -= v * 2
            if cnt[i] == 1:
                ch = c
        sb = t
        if ch:
            sb += ch
        for i in range(len(t) - 1, -1, -1):
            sb += t[i]
        return sb
