# LeetCode 3029 - Minimum Time to Revert Word to Initial State I
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        i = k
        while i < n:
            if word[i:] == word[: n - i]:
                return i // k
            i += k
        return (n + k - 1) // k
