# LeetCode 0266 - Palindrome Permutation
# https://leetcode.com/problems/palindrome-permutation/


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord("a")] += 1
        odd = sum(count % 2 for count in counts)
        return odd <= 1
