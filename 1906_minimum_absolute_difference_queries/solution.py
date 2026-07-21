from typing import List

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        pref = [[0] * 101 for _ in range(n + 1)]
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i][:]
            pref[i + 1][x] += 1
        ans = []
        for left, right in queries:
            prev = -1
            best = float("inf")
            for value in range(1, 101):
                if pref[right + 1][value] - pref[left][value] > 0:
                    if prev != -1:
                        best = min(best, value - prev)
                    prev = value
            ans.append(-1 if best == float("inf") else best)
        return ans
