# LeetCode 0131 - Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: list[list[str]] = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int, path: list[str]) -> None:
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start : end + 1])
                    dfs(end + 1, path)
                    path.pop()

        dfs(0, [])
        return result
