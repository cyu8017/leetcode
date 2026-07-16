from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0
        seen, prefix, answer = {0: -1}, 0, len(nums)
        for i, x in enumerate(nums):
            prefix = (prefix + x) % p
            need = (prefix - target) % p
            if need in seen:
                answer = min(answer, i - seen[need])
            seen[prefix] = i
        return answer if answer < len(nums) else -1
