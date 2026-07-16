# LeetCode 0388 - Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack: list[int] = []
        max_length = 0

        for line in input.split("\n"):
            depth = line.count("\t")
            name = line[depth:]
            while len(stack) > depth:
                stack.pop()

            if "." in name:
                total = len(name) + (stack[-1] if stack else 0)
                max_length = max(max_length, total)
            else:
                prefix = stack[-1] if stack else 0
                stack.append(prefix + len(name) + 1)

        return max_length
