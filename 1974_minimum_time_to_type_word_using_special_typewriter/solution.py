class Solution:
    def minTimeToType(self, word: str) -> int:
        cur = "a"
        ans = 0
        for ch in word:
            d = abs(ord(ch) - ord(cur))
            ans += min(d, 26 - d) + 1
            cur = ch
        return ans
