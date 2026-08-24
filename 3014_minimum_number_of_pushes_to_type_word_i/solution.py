# LeetCode 3014 - Minimum Number of Pushes to Type Word I
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        k = 1
        for i in range(n // 8):
            ans += k * 8
            k += 1
        ans += k * (n % 8)
        return ans
