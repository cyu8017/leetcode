# LeetCode 0722 - Remove Comments
# https://leetcode.com/problems/remove-comments/

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result: list[str] = []
        buffer: list[str] = []
        in_block = False

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i : i + 2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                elif i + 1 < len(line) and line[i : i + 2] == "/*":
                    in_block = True
                    i += 2
                elif i + 1 < len(line) and line[i : i + 2] == "//":
                    break
                else:
                    buffer.append(line[i])
                    i += 1

            if not in_block and buffer:
                result.append("".join(buffer))
                buffer = []

        return result
