from typing import List

class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        first = {0: -1}
        ans = s = 0
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            s += a - b
            if s in first:
                ans = max(ans, i - first[s])
            else:
                first[s] = i
        return ans
