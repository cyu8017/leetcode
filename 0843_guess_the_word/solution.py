# LeetCode 0843 - Guess the Word
# https://leetcode.com/problems/guess-the-word/

class Solution:
    def findSecretWord(self, words: list[str], master) -> None:
        def match(a: str, b: str) -> int:
            return sum(x == y for x, y in zip(a, b))

        candidates = words[:]
        while candidates:
            # Pick the guess that minimizes the size of the largest remaining bucket.
            best = min(
                candidates,
                key=lambda w: max(
                    sum(1 for c in candidates if match(w, c) == m) for m in range(7)
                ),
            )
            score = master.guess(best)
            if score == 6:
                return
            candidates = [c for c in candidates if match(c, best) == score]
