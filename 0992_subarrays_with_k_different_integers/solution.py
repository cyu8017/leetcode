# LeetCode 0992 - Subarrays with K Different Integers
# https://leetcode.com/problems/subarrays-with-k-different-integers/

from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def at_most(m: int) -> int:
            count: dict[int, int] = defaultdict(int)
            left = ans = 0
            for right, x in enumerate(nums):
                count[x] += 1
                while len(count) > m:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                ans += right - left + 1
            return ans

        return at_most(k) - at_most(k - 1)
