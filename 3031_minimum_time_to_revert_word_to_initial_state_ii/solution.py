# LeetCode 3031 - Minimum Time to Revert Word to Initial State II
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/


class Hashing:
    def __init__(self, word: str, bas: int, mod: int):
        self.mod = mod
        n = len(word)
        self.p = [0] * (n + 1)
        self.h = [0] * (n + 1)
        self.p[0] = 1
        self.h[0] = 0
        B = bas
        M = mod
        for i in range(1, n + 1):
            self.p[i] = self.p[i - 1] * B % M
            self.h[i] = (self.h[i - 1] * B + (ord(word[i - 1]) - 97)) % M

    def query(self, l: int, r: int) -> int:
        M = self.mod
        return (self.h[r] - self.h[l - 1] * self.p[r - l + 1] % M + M) % M


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        hashing = Hashing(word, 13331, 998244353)
        n = len(word)
        i = k
        while i < n:
            if hashing.query(1, n - i) == hashing.query(i + 1, n):
                return i // k
            i += k
        return (n + k - 1) // k
