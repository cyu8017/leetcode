# LeetCode 2648 - Generate Fibonacci Sequence
# https://leetcode.com/problems/generate-fibonacci-sequence/

from typing import Generator, Iterator


class Solution:
    def fibGenerator(self) -> Iterator[int]:
        def gen() -> Generator[int, None, None]:
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b

        return gen()
