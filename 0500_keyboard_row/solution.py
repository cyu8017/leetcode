# LeetCode 0500 - Keyboard Row
# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]

        def on_one_row(word: str) -> bool:
            letters = {ch.lower() for ch in word if ch.isalpha()}
            return any(letters <= row for row in rows)

        return [word for word in words if on_one_row(word)]
