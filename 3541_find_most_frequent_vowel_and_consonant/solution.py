# LeetCode 3541 - Find Most Frequent Vowel and Consonant
# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/


class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
        a = b = 0
        for i in range(26):
            c = chr(97 + i)
            if c in "aeiou":
                a = max(a, cnt[i])
            else:
                b = max(b, cnt[i])
        return a + b
