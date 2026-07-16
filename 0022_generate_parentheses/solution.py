# LeetCode 0022 - Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        def backtrack(path: list[str], open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return result
