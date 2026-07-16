from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = Counter(letters)
        counts = [Counter(word) for word in words]
        values = [sum(score[ord(ch) - 97] for ch in word) for word in words]
        def dfs(i: int) -> int:
            if i == len(words):
                return 0
            best = dfs(i + 1)
            if counts[i] <= available:
                available.subtract(counts[i])
                best = max(best, values[i] + dfs(i + 1))
                available.update(counts[i])
            return best
        return dfs(0)
