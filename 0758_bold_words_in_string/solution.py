# LeetCode 0758 - Bold Words in String
# https://leetcode.com/problems/bold-words-in-string/

from typing import List


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        bold = [False] * n
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)

        parts: list[str] = []
        i = 0
        while i < n:
            if bold[i]:
                parts.append("<b>")
                while i < n and bold[i]:
                    parts.append(s[i])
                    i += 1
                parts.append("</b>")
            else:
                parts.append(s[i])
                i += 1
        # LeetCode uses <b></b>; local cases use ** markdown bold.
        return "".join(parts).replace("<b>", "**").replace("</b>", "**")
