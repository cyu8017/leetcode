from typing import List, Optional

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cur = sum(c in vowels for c in s[:k])
        ans = cur
        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i-k] in vowels)
            ans = max(ans, cur)
        return ans
