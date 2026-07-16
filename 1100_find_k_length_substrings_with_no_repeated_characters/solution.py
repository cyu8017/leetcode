# LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        from collections import Counter

        window = Counter(s[:k])
        ans = 1 if len(window) == k else 0
        for i in range(k, len(s)):
            window[s[i]] += 1
            left = s[i - k]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if len(window) == k:
                ans += 1
        return ans
