# LeetCode 0523 - Continuous Subarray Sum
# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix = 0
        remainders = {0: -1}
        for index, num in enumerate(nums):
            prefix += num
            mod = prefix % k if k else prefix
            if mod in remainders:
                if index - remainders[mod] >= 2:
                    return True
            else:
                remainders[mod] = index
        return False
