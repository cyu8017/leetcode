from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        lengths, answer = {}, -1
        for step, x in enumerate(arr, 1):
            left, right = lengths.get(x - 1, 0), lengths.get(x + 1, 0)
            size = left + 1 + right
            lengths[x - left] = lengths[x + right] = size
            if left == m or right == m:
                answer = step - 1
        return answer
