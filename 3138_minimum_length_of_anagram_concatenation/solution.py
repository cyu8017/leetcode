# LeetCode 3138 - Minimum Length of Anagram Concatenation
# https://leetcode.com/problems/minimum-length-of-anagram-concatenation/


class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        def check(k: int) -> bool:
            for i in range(0, n, k):
                cnt1 = [0] * 26
                for j in range(i, i + k):
                    cnt1[ord(s[j]) - 97] += 1
                for j in range(26):
                    if cnt1[j] * (n // k) != cnt[j]:
                        return False
            return True

        i = 1
        while True:
            if n % i == 0 and check(i):
                return i
            i += 1
