from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(skip: int) -> bool:
            prev = None
            for i, x in enumerate(nums):
                if i == skip:
                    continue
                if prev is not None and x <= prev:
                    return False
                prev = x
            return True

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return check(i - 1) or check(i)
        return True
