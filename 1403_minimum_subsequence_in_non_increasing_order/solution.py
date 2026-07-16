class Solution:
    def minSubsequence(self, nums):
        answer, chosen, total = [], 0, sum(nums)
        for value in sorted(nums, reverse=True):
            answer.append(value)
            chosen += value
            if chosen > total - chosen:
                return answer
