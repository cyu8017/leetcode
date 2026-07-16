from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca, cb = Counter(a), Counter(b)
        n, m = len(a), len(b)
        ans = n + m - max(max(ca.values()), max(cb.values()))
        pre_a = pre_b = 0
        for code in range(25):
            ch = chr(ord("a") + code)
            pre_a += ca[ch]
            pre_b += cb[ch]
            ans = min(ans, n - pre_a + pre_b, m - pre_b + pre_a)
        return ans
