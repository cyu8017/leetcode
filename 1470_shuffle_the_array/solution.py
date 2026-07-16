from typing import List, Optional

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [v for pair in zip(nums[:n], nums[n:]) for v in pair]
