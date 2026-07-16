# LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def best(a: int, b: int) -> int:
            best_a = ans = 0
            for i in range(a + b, len(prefix)):
                best_a = max(best_a, prefix[i - b] - prefix[i - b - a])
                ans = max(ans, best_a + prefix[i] - prefix[i - b])
            return ans

        return max(best(firstLen, secondLen), best(secondLen, firstLen))
