# LeetCode 2197 - Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

from typing import List
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b != 0:
                t = a % b
                a = b
                b = t
            return a

        stack = []
        for x0 in nums:
            x = x0
            while stack:
                g = gcd(stack[len(stack) - 1], x)
                if g == 1:
                    break
                x = stack[len(stack) - 1] // g * x
                stack.pop()
            stack.append(x)
        return stack
