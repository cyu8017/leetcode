# LeetCode 0548 - Split Array with Equal Sum
# https://leetcode.com/problems/split-array-with-equal-sum/

from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False

        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)

        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                first = prefix[i] - prefix[0]
                second = prefix[j] - prefix[i + 1]
                if first == second:
                    seen.add(first)

            for k in range(j + 2, n - 1):
                third = prefix[k] - prefix[j + 1]
                fourth = prefix[n] - prefix[k + 1]
                if third == fourth and third in seen:
                    return True

        return False
