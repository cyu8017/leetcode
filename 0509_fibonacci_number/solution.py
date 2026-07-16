# LeetCode 0509 - Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        previous, current = 0, 1
        for _ in range(2, n + 1):
            previous, current = current, previous + current
        return current
