class Solution:
    def minElements(self, nums, limit, goal):
        diff = abs(sum(nums) - goal)
        return (diff + limit - 1) // limit
