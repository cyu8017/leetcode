class Solution:
    def kLengthApart(self, nums, k):
        previous = -k - 1
        for i, value in enumerate(nums):
            if value:
                if i - previous <= k:
                    return False
                previous = i
        return True
