# LeetCode 0660 - Remove 9
# https://leetcode.com/problems/remove-9/


class Solution:
    def newInteger(self, n: int) -> int:
        digits: list[str] = []
        while n:
            digits.append(str(n % 9))
            n //= 9
        return int("".join(reversed(digits))) if digits else 0
