# LeetCode 3330 - Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/


class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                ans += 1
        return ans
