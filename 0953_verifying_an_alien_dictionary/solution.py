# LeetCode 0953 - Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        rank = {c: i for i, c in enumerate(order)}

        def key(w: str) -> list[int]:
            return [rank[c] for c in w]

        return all(key(words[i]) <= key(words[i + 1]) for i in range(len(words) - 1))
