# LeetCode 0068 - Text Justification
# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result: List[str] = []
        i = 0

        while i < len(words):
            line_words: List[str] = []
            line_len = 0

            while i < len(words):
                word = words[i]
                extra = 1 if line_words else 0
                if line_len + len(word) + extra > maxWidth:
                    break
                line_words.append(word)
                line_len += len(word) + extra
                i += 1

            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_chars = sum(len(word) for word in line_words)
                total_spaces = maxWidth - total_chars
                gaps = len(line_words) - 1
                space, remainder = divmod(total_spaces, gaps)
                line = ""
                for j, word in enumerate(line_words[:-1]):
                    line += word + " " * (space + (1 if j < remainder else 0))
                line += line_words[-1]

            result.append(line)

        return result
