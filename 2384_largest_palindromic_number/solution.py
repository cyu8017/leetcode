# LeetCode 2384 - Largest Palindromic Number
# https://leetcode.com/problems/largest-palindromic-number/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10
        for ch in num:
            freq[ord(ch) - 48] += 1
        left = ""
        for d in range(9, -1, -1):
            pairs = freq[d] // 2
            left += str(d) * pairs
            freq[d] %= 2
        mid = ""
        for d in range(9, -1, -1):
            if freq[d] > 0:
                mid = str(d)
                break
        if not left:
            return mid if mid else "0"
        if left[0] == "0":
            return mid if mid else "0"
        return left + mid + left[::-1]
