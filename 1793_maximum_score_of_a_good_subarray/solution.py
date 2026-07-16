class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        stack = []
        ans = 0
        for i in range(n + 1):
            while stack and (i == n or nums[i] < nums[stack[-1]]):
                mid = stack.pop()
                left = stack[-1] + 1 if stack else 0
                right = i - 1
                if left <= k <= right:
                    ans = max(ans, nums[mid] * (right - left + 1))
            stack.append(i)
        return ans
