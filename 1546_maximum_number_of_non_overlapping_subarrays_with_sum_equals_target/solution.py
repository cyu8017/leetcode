# LeetCode 1546

class Solution:
    def maxNonOverlapping(self, nums, target):
        seen = {0}
        prefix = answer = 0
        for value in nums:
            prefix += value
            if prefix - target in seen:
                answer += 1
                prefix = 0
                seen = {0}
            else:
                seen.add(prefix)
        return answer
