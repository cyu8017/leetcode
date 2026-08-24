# LeetCode 2950 - Number of Divisible Substrings
# https://leetcode.com/problems/number-of-divisible-substrings/


class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        vals = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
        ans = 0
        n = len(word)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += vals[ord(word[j]) - 97]
                if s % (j - i + 1) == 0:
                    ans += 1
        return ans
