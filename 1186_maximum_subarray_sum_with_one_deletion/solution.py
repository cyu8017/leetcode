# LeetCode 1186 - Maximum Subarray Sum with One Deletion
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        keep = delete = ans = arr[0]
        for x in arr[1:]:
            delete = max(keep, delete + x)
            keep = max(keep + x, x)
            ans = max(ans, keep, delete)
        return ans
