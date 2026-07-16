# LeetCode 1316 - Distinct Echo Substrings

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        mod1, mod2, base = 1_000_000_007, 1_000_000_009, 911382323
        h1 = [0] * (n + 1); h2 = [0] * (n + 1)
        p1 = [1] * (n + 1); p2 = [1] * (n + 1)
        for i, ch in enumerate(text):
            code = ord(ch)
            h1[i+1] = (h1[i] * base + code) % mod1
            h2[i+1] = (h2[i] * base + code) % mod2
            p1[i+1] = p1[i] * base % mod1
            p2[i+1] = p2[i] * base % mod2
        def hashed(left, right):
            length = right - left
            return ((h1[right] - h1[left] * p1[length]) % mod1,
                    (h2[right] - h2[left] * p2[length]) % mod2)
        echoes = set()
        for half in range(1, n // 2 + 1):
            for left in range(n - 2 * half + 1):
                if hashed(left, left + half) == hashed(left + half, left + 2 * half):
                    echoes.add((2 * half,) + hashed(left, left + 2 * half))
        return len(echoes)
