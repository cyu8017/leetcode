# LeetCode 0202 - Happy Number
# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        def next_value(value: int) -> int:
            total = 0
            while value:
                digit = value % 10
                total += digit * digit
                value //= 10
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = next_value(n)
        return n == 1
