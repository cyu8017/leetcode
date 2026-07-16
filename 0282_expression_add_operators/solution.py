# LeetCode 0282 - Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result: list[str] = []

        def backtrack(index: int, path: str, value: int, previous: int) -> None:
            if index == len(num):
                if value == target:
                    result.append(path)
                return
            for end in range(index, len(num)):
                if end > index and num[index] == "0":
                    break
                current_str = num[index : end + 1]
                current = int(current_str)
                if index == 0:
                    backtrack(end + 1, current_str, current, current)
                else:
                    backtrack(end + 1, path + "+" + current_str, value + current, current)
                    backtrack(end + 1, path + "-" + current_str, value - current, -current)
                    backtrack(
                        end + 1,
                        path + "*" + current_str,
                        value - previous + previous * current,
                        previous * current,
                    )

        backtrack(0, "", 0, 0)
        return result
