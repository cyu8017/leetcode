# LeetCode 2803 - Factorial Generator
# https://leetcode.com/problems/factorial-generator/

from typing import Generator, List


class Solution:
    def factorialGenerator(self, n: int) -> List[int]:
        def gen() -> Generator[int, None, None]:
            cur = 1
            if n == 0:
                yield 1
                return
            for i in range(1, n + 1):
                cur *= i
                yield cur

        return list(gen())
