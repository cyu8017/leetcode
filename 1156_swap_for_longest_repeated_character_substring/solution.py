# LeetCode 1156 - Swap For Longest Repeated Character Substring
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        n = len(text)
        ans = 0
        i = 0
        while i < n:
            j = i
            while j < n and text[j] == text[i]:
                j += 1
            length = j - i
            k = j + 1
            while k < n and text[k] == text[i]:
                k += 1
            length2 = k - j - 1 if j < n else 0
            ans = max(ans, min(length + length2 + 1, count[text[i]]))
            i = j
        return ans
