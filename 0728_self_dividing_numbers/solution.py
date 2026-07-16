# LeetCode 0728 - Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            x = num
            while x:
                digit = x % 10
                if digit == 0 or num % digit != 0:
                    return False
                x //= 10
            return True

        return [num for num in range(left, right + 1) if is_self_dividing(num)]
