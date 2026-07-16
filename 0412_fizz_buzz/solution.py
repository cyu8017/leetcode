# LeetCode 0412 - Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result: list[str] = []
        for value in range(1, n + 1):
            if value % 15 == 0:
                result.append("FizzBuzz")
            elif value % 3 == 0:
                result.append("Fizz")
            elif value % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(value))
        return result
