# LeetCode 2269 - Find the K-Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(len(s) - k + 1):
            sub = 0
            for j in range(k):
                sub = sub * 10 + (ord(s[i + j]) - 48)
            if sub != 0 and num % sub == 0:
                ans += 1
        return ans
