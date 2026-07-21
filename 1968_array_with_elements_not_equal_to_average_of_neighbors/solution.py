from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        small, large = nums[:mid], nums[mid:]
        ans: List[int] = []
        i = j = 0
        while i < len(small) or j < len(large):
            if i < len(small):
                ans.append(small[i])
                i += 1
            if j < len(large):
                ans.append(large[j])
                j += 1
        return ans
