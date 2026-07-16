# LeetCode 0804 - Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        return len({"".join(codes[ord(ch) - 97] for ch in word) for word in words})
