from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        queue = deque()
        best = nums[:]
        for i, value in enumerate(nums):
            while queue and queue[0] < i - k:
                queue.popleft()
            best[i] = value + max(0, best[queue[0]] if queue else 0)
            while queue and best[queue[-1]] <= best[i]:
                queue.pop()
            queue.append(i)
        return max(best)
