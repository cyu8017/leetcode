from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        low, high = deque(), deque()
        left = answer = 0
        for right, value in enumerate(nums):
            while low and nums[low[-1]] > value:
                low.pop()
            while high and nums[high[-1]] < value:
                high.pop()
            low.append(right)
            high.append(right)
            while nums[high[0]] - nums[low[0]] > limit:
                left += 1
                if low[0] < left:
                    low.popleft()
                if high[0] < left:
                    high.popleft()
            answer = max(answer, right - left + 1)
        return answer
