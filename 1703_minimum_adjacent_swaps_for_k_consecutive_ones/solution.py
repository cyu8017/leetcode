from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [i for i, v in enumerate(nums) if v == 1]
        adjusted = [pos - i for i, pos in enumerate(ones)]
        prefix = [0]
        for value in adjusted:
            prefix.append(prefix[-1] + value)
        best = 10 ** 30
        for left in range(len(ones) - k + 1):
            right = left + k
            mid = left + k // 2
            median = adjusted[mid]
            cost = median * (mid - left) - (prefix[mid] - prefix[left])
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1)
            best = min(best, cost)
        return best
