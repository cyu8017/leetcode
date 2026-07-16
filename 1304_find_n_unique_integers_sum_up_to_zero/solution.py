# LeetCode 1304 - Find N Unique Integers Sum Up To Zero

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for value in range(1, n // 2 + 1):
            answer.extend((-value, value))
        if n % 2:
            answer.append(0)
        return answer
