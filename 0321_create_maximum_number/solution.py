# LeetCode 0321 - Create Maximum Number
# https://leetcode.com/problems/create-maximum-number/

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(values: List[int], count: int) -> List[int]:
            drop = len(values) - count
            stack: list[int] = []
            for value in values:
                while drop and stack and stack[-1] < value:
                    stack.pop()
                    drop -= 1
                stack.append(value)
            return stack[:count]

        def merge(first: List[int], second: List[int]) -> List[int]:
            result: list[int] = []
            left = right = 0
            while left < len(first) and right < len(second):
                if first[left:] > second[right:]:
                    result.append(first[left])
                    left += 1
                else:
                    result.append(second[right])
                    right += 1
            result.extend(first[left:])
            result.extend(second[right:])
            return result

        best: list[int] = []
        for take_first in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            take_second = k - take_first
            candidate = merge(pick_max(nums1, take_first), pick_max(nums2, take_second))
            if candidate > best:
                best = candidate
        return best
