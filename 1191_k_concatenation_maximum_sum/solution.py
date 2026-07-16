# LeetCode 1191 - K-Concatenation Maximum Sum
# https://leetcode.com/problems/k-concatenation-maximum-sum/

class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums: list[int]) -> int:
            best = cur = 0
            for x in nums:
                cur = max(0, cur + x)
                best = max(best, cur)
            return best

        one = kadane(arr)
        if k == 1:
            return one % MOD
        two = kadane(arr + arr)
        total = sum(arr)
        if total > 0:
            return max(one, two + total * (k - 2)) % MOD
        return max(one, two) % MOD
