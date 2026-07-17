# LeetCode 1830 - Minimum Number of Operations to Make String Sorted
# https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/


class Solution:
    def makeStringSorted(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)

        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % mod

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        ans = 0
        for i, ch in enumerate(s):
            c = ord(ch) - ord("a")
            for smaller in range(c):
                if freq[smaller] == 0:
                    continue
                freq[smaller] -= 1
                ways = fact[n - i - 1]
                for count in freq:
                    ways = ways * inv_fact[count] % mod
                ans = (ans + ways) % mod
                freq[smaller] += 1
            freq[c] -= 1

        return ans
