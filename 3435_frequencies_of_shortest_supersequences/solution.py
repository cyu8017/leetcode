# LeetCode 3435 - Frequencies of Shortest Supersequences
# https://leetcode.com/problems/frequencies-of-shortest-supersequences/

from typing import List


class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        used = [False] * 26
        for w in words:
            used[ord(w[0]) - 97] = True
            used[ord(w[1]) - 97] = True
        letters = [i for i in range(26) if used[i]]
        m = len(letters)
        freq = [0] * 26
        best = 10**9
        best_freqs: List[List[int]] = []

        def dfs(i: int) -> None:
            nonlocal best, best_freqs
            if i == m:
                for w in words:
                    a = ord(w[0]) - 97
                    b = ord(w[1]) - 97
                    if a == b:
                        if freq[a] < 2:
                            return
                    elif freq[a] < 1 or freq[b] < 1:
                        return
                s = sum(freq)
                f = freq[:]
                if s < best:
                    best = s
                    best_freqs = [f]
                elif s == best:
                    best_freqs.append(f)
                return
            L = letters[i]
            for c in range(1, 3):
                freq[L] = c
                dfs(i + 1)
            freq[L] = 0

        dfs(0)
        return best_freqs
