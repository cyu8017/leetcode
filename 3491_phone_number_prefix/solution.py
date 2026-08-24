# LeetCode 3491 - Phone Number Prefix
# https://leetcode.com/problems/phone-number-prefix/

from typing import List


class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers = sorted(numbers)
        for i in range(len(numbers) - 1):
            if len(numbers[i]) <= len(numbers[i + 1]) and numbers[i + 1].startswith(numbers[i]):
                return False
        return True
