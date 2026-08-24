# LeetCode 2156 - Find Substring With Given Hash Value
# https://leetcode.com/problems/find-substring-with-given-hash-value/
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        pk = 1
        for i in range(k - 1):
            pk = pk * power % modulo
        h = 0
        ans = 0
        for i in range(n - 1, (n - k) - 1, -1):
            h = (h * power + (ord(s[i]) - 96)) % modulo
        if h == hashValue:
            ans = n - k
        for i in range(n - k - 1, (0) - 1, -1):
            h = (h - (ord(s[i + k]) - 96) * pk % modulo + modulo) % modulo
            h = (h * power + (ord(s[i]) - 96)) % modulo
            if h == hashValue:
                ans = i
        return s[ans:ans + k]
