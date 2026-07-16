# LeetCode 0599 - Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = {name: i for i, name in enumerate(list1)}
        best = float("inf")
        answer: list[str] = []

        for j, name in enumerate(list2):
            if name not in index1:
                continue
            total = index1[name] + j
            if total < best:
                best = total
                answer = [name]
            elif total == best:
                answer.append(name)

        return answer
