from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)
        ans = []
        for candy_type, day, cap in queries:
            min_eaten = day + 1
            max_eaten = (day + 1) * cap
            ans.append(max_eaten > prefix[candy_type] and min_eaten <= prefix[candy_type + 1])
        return ans
