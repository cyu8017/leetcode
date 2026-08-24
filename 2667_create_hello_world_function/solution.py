# LeetCode 2667 - Create Hello World Function
# https://leetcode.com/problems/create-hello-world-function/

from typing import Any, Callable


class Solution:
    def createHelloWorld(self) -> Callable:
        def hello(*args: Any) -> str:
            return "Hello World"

        return hello
