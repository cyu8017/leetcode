# LeetCode 0616 - Add Bold Tag in String
# https://leetcode.com/problems/add-bold-tag-in-string/

from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
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

        return "".join(parts)
