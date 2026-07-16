# LeetCode 0402 - Remove K Digits
# https://leetcode.com/problems/remove-k-digits/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: list[str] = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")
        return result or "0"
