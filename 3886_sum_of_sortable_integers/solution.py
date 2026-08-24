# LeetCode 3886 - Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-sortable-integers/

from typing import List


class Solution:
    def sumOfSortableIntegers(self, nums: List[int]) -> int:
        def rotation_matches(block: List[int], target: List[int]) -> bool:
            k = len(block)
            prefix = [0] * k
            for i in range(1, k):
                j = prefix[i - 1]
                while j > 0 and target[i] != target[j]:
                    j = prefix[j - 1]
                if target[i] == target[j]:
                    j += 1
                prefix[i] = j
            matched = 0
            for i in range(2 * k - 1):
                x = block[i % k]
                while matched > 0 and x != target[matched]:
                    matched = prefix[matched - 1]
                if x == target[matched]:
                    matched += 1
                if matched == k:
                    return True
            return False

        n = len(nums)
        sorted_nums = sorted(nums)
        divisors: List[int] = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1
        answer = 0
        for k in divisors:
            ok = True
            for start in range(0, n, k):
                block = nums[start : start + k]
                target = sorted_nums[start : start + k]
                if not rotation_matches(block, target):
                    ok = False
                    break
            if ok:
                answer += k
        return answer
