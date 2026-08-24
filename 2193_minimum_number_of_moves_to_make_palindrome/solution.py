# LeetCode 2193 - Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        b = list(s)
        ans = 0
        while len(b) > 1:
            j = len(b) - 1
            while j > 0 and b[j] != b[0]:
                j -= 1
            if j == 0:
                ans += len(b) // 2
                b.pop(0)
                continue
            ans += len(b) - 1 - j
            b.pop(j)
            b.pop(0)
        return ans
