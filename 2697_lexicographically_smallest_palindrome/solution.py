# LeetCode 2697 - Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        n = len(arr)
        for i in range(n // 2):
            c = arr[i] if arr[i] < arr[n - 1 - i] else arr[n - 1 - i]
            arr[i] = arr[n - 1 - i] = c
        return "".join(arr)
