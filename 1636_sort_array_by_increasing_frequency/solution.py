class Solution:
    def frequencySort(self, nums):
        from collections import Counter
        count=Counter(nums)
        return sorted(nums,key=lambda x:(count[x],-x))
