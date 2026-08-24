# LeetCode 3216 - Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        for i in range(1, n):
            a, b = arr[i - 1], arr[i]
            if a > b and (ord(a) % 2) == (ord(b) % 2):
                arr[i - 1], arr[i] = b, a
                return "".join(arr)
        return s
