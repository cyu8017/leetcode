from typing import List

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        rest = total - mx
        if mx > rest + 1:
            return 2 * rest + 1
        return total
