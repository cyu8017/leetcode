# LeetCode 0017 - Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result: list[str] = []

        def backtrack(index: int, path: list[str]) -> None:
            if index == len(digits):
                result.append("".join(path))
                return
            for ch in mapping[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result
