class Solution:
    def specialArray(self, nums):
        return next((x for x in range(len(nums) + 1) if sum(v >= x for v in nums) == x), -1)
