from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        total = 0
        for arrival, cook in customers:
            current = max(current, arrival) + cook
            total += current - arrival
        return total / len(customers)
