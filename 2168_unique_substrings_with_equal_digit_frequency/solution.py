# LeetCode 2168 - Unique Substrings With Equal Digit Frequency
# https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        seen = set()
        for i in range(n):
            freq = [0] * (10)
            maxf = 0
            kinds = 0
            for j in range(i, n):
                d = ord(s[j]) - 48
                if freq[d] == 0:
                    kinds += 1
                freq[d] += 1
                maxf = max(maxf, freq[d])
                if maxf * kinds == j - i + 1:
                    seen.add(s[i:j + 1])
        return len(seen)
