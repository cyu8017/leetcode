from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive = negative = answer = 0
        for x in nums:
            if x == 0:
                positive = negative = 0
            elif x > 0:
                positive += 1
                negative = negative + 1 if negative else 0
            else:
                positive, negative = (negative + 1 if negative else 0), positive + 1
            answer = max(answer, positive)
        return answer
