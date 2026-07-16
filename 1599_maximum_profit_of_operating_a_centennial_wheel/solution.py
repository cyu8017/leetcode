from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = profit = best = answer = rotation = 0
        i = 0
        while i < len(customers) or waiting:
            if i < len(customers):
                waiting += customers[i]
            boarded = min(4, waiting)
            waiting -= boarded
            rotation += 1
            profit += boarded * boardingCost - runningCost
            if profit > best:
                best, answer = profit, rotation
            i += 1
        return answer if best > 0 else -1
