# LeetCode 1165 - Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {ch: i for i, ch in enumerate(keyboard)}
        ans = prev = 0
        for ch in word:
            ans += abs(pos[ch] - prev)
            prev = pos[ch]
        return ans
