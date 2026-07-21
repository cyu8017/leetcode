class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1
        mask = ans = 0
        for ch in word:
            mask ^= 1 << (ord(ch) - 97)
            ans += count[mask]
            for bit in range(10):
                ans += count[mask ^ (1 << bit)]
            count[mask] += 1
        return ans
